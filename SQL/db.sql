CREATE TABLE lComplains(
ref_num INT AUTO_INCREMENT PRIMARY KEY, 
dte NVARCHAR(50),
f_name NVARCHAR(255),
l_name NVARCHAR(255),
mobile_num NVARCHAR(50),
address NVARCHAR(255),
light_num NVARCHAR(100),
description NVARCHAR(255),
state_value BOOLEAN);


INSERT INTO lComplains (dte, f_name, l_name, mobile_num, address, light_num, description, state_value) VALUES ('2021-10-05','SACHINDU','KAVISHKA','0764314505','No 447 Mahahunupitiya, Negombo','5245','blah blah balh','1');  

INSERT INTO lComplains (dte