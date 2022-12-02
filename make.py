from zipfile import ZipFile

# # Template for a new Lambda (can be copied and pasted for each new lambda)
#zipObj = ZipFile('Deploy/[NAME OF LAMBDA].zip', 'w')
#zipObj.write('[FULL PATH OF FILE]', '[FILE NAME WITHOUT PATH]')
# # Repeat the above line for each file that is referenced by the lambda
#zipObj.close()

##LOGIN LAMBDA
# create a ZipFile object
zipObj = ZipFile('Deploy/Login.zip', 'w')
# Add multiple files to the zip
zipObj.write('Controllers/BaseController.py', 'BaseController.py')
zipObj.write('Model/DAO/Factory/DynamoFactory.py', 'DynamoFactory.py')
zipObj.write('Model/DAO/Factory/AbstractFactory.py', 'AbstractFactory.py')
zipObj.write('Controllers/LoginController.py', 'LoginController.py')
zipObj.write('Model/Service/LoginService.py', 'LoginService.py')
zipObj.write('Model/User.py', 'User.py')
zipObj.write('Model/DAO/UserDAO.py', 'UserDAO.py')
# close the Zip File
zipObj.close()

##REGISTER LAMBDA
# create a ZipFile object
zipObj = ZipFile('Deploy/Register.zip', 'w')
# Add multiple files to the zip
zipObj.write('Controllers/BaseController.py', 'BaseController.py')
zipObj.write('Model/DAO/Factory/DynamoFactory.py', 'DynamoFactory.py')
zipObj.write('Model/DAO/Factory/AbstractFactory.py', 'AbstractFactory.py')
zipObj.write('Controllers/LoginController.py', 'LoginController.py')
zipObj.write('Model/Service/LoginService.py', 'LoginService.py')
zipObj.write('Model/User.py', 'User.py')
zipObj.write('Model/DAO/UserDAO.py', 'UserDAO.py')
# close the Zip File
zipObj.close()


##SKILLS LAMBDA
# create a ZipFile object
zipObj = ZipFile('Deploy/Skills.zip', 'w')
# Add multiple files to the zip
zipObj.write('Controllers/BaseController.py', 'BaseController.py')
zipObj.write('Model/DAO/Factory/DynamoFactory.py', 'DynamoFactory.py')
zipObj.write('Model/DAO/Factory/AbstractFactory.py', 'AbstractFactory.py')
zipObj.write('Controllers/SkillController.py', 'SkillController.py')
zipObj.write('Model/Service/SkillService.py', 'SkillService.py')
zipObj.write('Model/Skill.py', 'Skill.py')
zipObj.write('Model/DAO/SkillDAO.py', 'SkillDAO.py')
# close the Zip File
zipObj.close()

