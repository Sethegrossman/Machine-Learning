# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:25:58 2020

@author: sethgrossman
"""
try:
    from selenium import webdriver
    import pandas as pd
    import time
      
    
    
    #%%
    driver = webdriver.Chrome()
    #%% reads in data
    complete_df = pd.read_csv('C:\\Users\\Seth Grossman\\Desktop\\SearchListMotorola.csv')
    complete_df = complete_df.set_index('Companies', drop = False)    
    
    #Make Company List
    companieslist = complete_df.iloc[:,0]
    companieslist = list(companieslist)
    
    #Make City List
    citieslist = complete_df.iloc[:,1]
    citieslist = list(citieslist)
    
    #Make Tab List
    Tab = complete_df.iloc[:,2]
    Tab = list(Tab)
    
    #Make NAICS List
    NAICS = complete_df.iloc[:,3]
    NAICS = list(NAICS)
    #%%
    
    #go to website
    driver.get('https://www-mergentonline-com.colorado.idm.oclc.org/advancedsearch.php#')
    
    
    #%%
    #login then continue
    loginusername = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/form/div[1]/input')
    loginusername.send_keys(input('Username'+'\n'))
    
    loginpassword = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/form/div[2]/input')
    loginpassword.send_keys(input('Password'+'\n'))
    
    continueclick = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/form/div[6]/button')
    continueclick.click()
    #%%
    
    #click the private database option
    DB_Private = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/div[1]/table/tbody/tr[4]/td[1]/input')
    DB_Private.click()
    
    
    #%% Select Advanced Search Criteria
    Search_Company_Name_Button = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[1]/td[2]/div/table/tbody/tr[1]/td[1]/a')
    
    Search_State_Name_Button = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[1]/a')
    
    Search_City_Name_Button = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td[1]/a')
    
    
    #Create the Input Options
    #%%
    Search_Company_Name_Button.click()
    
    
    Search_State_Name_Button.click()
    Search_State_Texas_Option = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[3]/select/option[45]')
    
    Search_State_Texas_Option.click()
    
    Search_City_Name_Button.click()
    
    
    
    
    #%%    
    
    df = pd.DataFrame(columns = ['Company', 'Revenue','Industry', 'Website', 'Phone', 'Street', 'City', 'State', 'Zipcode', 'Tab', 'NAICS'])
    
    
    for i in range (len(companieslist)):
    
        revenue_output = 0
        contact_info_output = 0
        industry_output = 0
        Street = 0
        City = 0
        State = 0
        Zipcode = 0
        Phone = 0
        Website = 0
        
        
        #find and enter the company names
        Search_Company_Name_Text_Box = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[4]/input')
        Search_Company_Name_Text_Box.clear()
        time.sleep(1)
        
        for a in range (len(str(companieslist[i]))):
            b = str(companieslist[i])
            Search_Company_Name_Text_Box.send_keys(b[a])
            time.sleep(0.15)
        time.sleep(0.5)
        
        #Find and enter city names
        Search_City_Name_Text_Box = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[4]/input')
        Search_City_Name_Text_Box.clear()
        time.sleep(1)
        
        for c in range (len(str(citieslist[i]))):
            d = str(citieslist[i])
            Search_City_Name_Text_Box.send_keys(d[c])
            time.sleep(0.15)
        time.sleep(0.5)
        
        #Submit search
        Search_Submit_Button = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[6]/input')
        Search_Submit_Button.click()
        viewsleep = ''
        
        while viewsleep == '':
            time.sleep(2)
            viewbutton = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[7]/div')
            viewsleep = viewbutton.text

        Search_View_Button = driver.find_element_by_xpath('/html/body/div[9]/div[4]/form/table[2]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[9]/a[2]')
        Search_View_Button.click()
    
    
        try:
            gotocompany = driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/table[2]/tbody/tr/td[2]/a')
            gotocompany.click()
        except:
            revenue_output = 'N/A'
    
        if revenue_output != 'N/A':
         
            try:
                revenue = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td')
                revenue_text = revenue.text
                revenue_output = revenue_text
                revenue_output = revenue_output[
                        revenue_output.index('$')+1:len(revenue_output)]
                revenue_output = revenue_output.replace(',','')
            except:
                revenue_output = revenue_text
               
            try:
                contact_info = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div')
                contact_info_output = contact_info.text
           
            except:
                contact_info_output = ''
                
            try: 
                Street = contact_info_output[
                        contact_info_output.index(' ')+1:
                        contact_info_output.index(',')
                        ]
            except: Street = 'N/A'
            
            try:
                City = contact_info_output[
                        contact_info_output.index(',')+2:
                        contact_info_output.index('TX')-1]
            except: City = 'N/A'
            
            State = 'TX'
            
            try:
                Zipcode = contact_info_output[
                        contact_info_output.index('TX')+3:
                        contact_info_output.index('|')-2
                        ]
            except: Zipcode = 'N/A'
            
            try:
                Phone = contact_info_output[
                        contact_info_output.index('Phone')+7:
                        contact_info_output.index('-',contact_info_output.find('Phone'))+5
                        ]
            except: Phone = 'N/A'
            
            try:
                Website = contact_info_output[
                        contact_info_output.index('Website')+9:
                        ]
            except: Website = 'N/A'
        
    
            try:
                industry = driver.find_element_by_id('summarycol2')
                industry_output = industry.text
                
                industry_output = industry_output[
                        industry_output.index('Primary SIC'):
                            ]
                
            except:
                industry_output = 'N/A'
    
    
                
        df = pd.DataFrame([{'Company': companieslist[i],
                         'Revenue': revenue_output,
                         'Industry': industry_output,
                         'Website' : Website,
                         'Phone' : Phone,
                         'Street' : Street,
                         'City' : City,
                         'State' : State,
                         'Zipcode' : Zipcode,
                         'Tab' : Tab[i],
                         'NAICS': NAICS[i]
                         }])
        
        df.to_csv('C:\\Users\\Seth Grossman\\Desktop\\CompanySearchMotorola.csv', index = False, mode = 'a', header = False)
    
        try:
            df.to_csv('C:\\Users\\Seth Grossman\\Desktop\\CheckingOutCompanySearchMotorola.csv', index = False, mode = 'a', header = False)
        except:
            pass
        
        time.sleep(3)
        driver.get('https://www-mergentonline-com.colorado.idm.oclc.org/advancedsearch.php#')
        
        
    #%%
    driver.close()
except:
    driver.close()