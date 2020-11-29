# url_shortener
A simple URL_SHORTENER written in Python with Flask.

## Infos
- URLS can be created on `/`
- All shourted urls can be found on `/r/<token>`. The token is shown in Green when you create an URL.

## Setup
- Install Docker on your System
- Navigate to the Projects root directory
- run `./docker-setup.sh`
- Your project should now be available on Port 80

## Configuration
A the moment you can only configure the maxlength of the token for your link in `URL_SHORTENER/app/config.py` by changing `self.url_length = 5`.

## License
All files under MIT License. https://github.com/NeonCrafter13/url_shortener/blob/master/LICENSE
