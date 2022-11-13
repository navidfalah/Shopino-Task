## shopino backend test
### url shortner
### this project created by django - django rest framework(drf)
### users
    we dont have any user model . just for superuser auth which has been developed by django itself
### links 
    algorithm of creating a string(slug) instead of a link has been designed by myself
    which goes in a while loop and select 2 char of the string and change it to alphabet using 
    ascii chars then goes in while loop to check if the link exists then add a random char if not 
    pass it back.
### views & endpoint
    there is one endpoint & one view
    endpoint is for creating a new link from an old one.
    and the view is for redirevting the page to the old one.
### why using counter instead of middleware?
    we can user middleware too. but when refreshing deoes matter.
    we are redirecting in this position. redirecting is like refresh so
    i prefer user a simple counter istead of middleware.
### api doc exists in open-api on this directory