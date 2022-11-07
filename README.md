# ArtU - Back End

This repo contains the backend of the ART-U (BYU CS428 Winter) App.

To deploy changes to AWS lambda, run 
> python make.py
from the base folder of the repo.  This will generate a .zip file inside of the Deploy folder with the name of the desired Lambda, and this .zip can be uploaded directly to lambda.

When a new file is imported to be used inside of a lambda, that file should be added to the make file for that lambda function as well.

When you are ready to deploy a new lambda, this should be done by adding a new section to the make file, following the template found at the beginning of the make file.