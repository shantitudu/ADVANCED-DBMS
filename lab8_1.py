#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given input as salary of three months (jan,feb,march),write a program that returns the total salary for quarter 1(Q1).
import mysql.connector


# In[4]:


cnx=mysql.connector.connect(host="localhost",user= "root",password="",database="lab1")


# In[5]:


cur=cnx.cursor()


# In[ ]:


cur.execute("""CREATE FUNCTION  calculate_Q_salary (jan_sal decimal,feb_sal decimal,march_sal decimal)
RETURNS DECIMAL
BEGIN
DECLARE Q_salary decimal;
SET Q_salary = jan_sal + feb_sal + march_sal;
RETURN Q_salary;
END;""")


# In[ ]:


cur.execute("""SELECT calculate_Q_salary(1500.00,2000.00,1000.00) AS Q_salary;""")


# In[ ]:


cur.close()


# In[ ]:


cnx.close()

