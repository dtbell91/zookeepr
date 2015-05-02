# Zookeepr Deployment Instructions
This document details how to deploy a Zookeepr instance with automated deployment from Github.

# Prerequisites
In order to continuously deploy Zookeepr, two separate Git repositories are required:
 - A public repo (eg. zookeepr/zookeepr); and
 - A private report (for storing the secret config files)

A cron job can will then be configured to maintain the Zookeepr code up to the currently desired commit by tags (eg. lca2016-prod or lca2016-uat), likewise for configuration from the private repo.

# Dependencies
Zookeepr has the following dependencies, here formatted into a friendly apt-get command
    ```
    sudo apt-get install apache2 libapache2-mod-python libapache2-mod-wsgi libpq-dev libpython-dev libxslt1-dev libxml2-dev postgresql git python-virtualenv
    ```

You should now have all of the required dependencies to run a Zookeepr instance successfully.

# The Steps
1. Create the zookeepr system account
    ```
    sudo adduser --disabled-password zookeepr
    ```

2. Login to the zookeepr user and pull down the git repo and prepare the environment
    ```
    sudo -u zookeepr -i
    git clone https://github.com/zookeepr/zookeepr.git
    cd zookeepr/
    virtualenv env --no-site-packages
    . ./env/bin/activate
    ```

3. Create the database (*please change the password to something suitably random in the below commands*)
    ```
    sudo -u postgres createuser --no-createdb --no-createrole --no-superuser zookeepr
    sudo -u postgres createdb -O zookeepr zk
    sudo -u postgres psql --command "ALTER USER zookeepr with PASSWORD 'zookeepr'"
    ```

4. Prepare the config files
    ```
    cp zkpylons/config/lca_info.py.sample zkpylons/config/lca_info.py
    cp development.ini.sample development.ini
    mkdir wsgi
    echo "from pyramid.paster import get_app
    application = get_app(
      '/home/zookeepr/zookeepr/development.ini', 'main')" > ./wsgi/zookeepr.wsgi
    ```

5. 
