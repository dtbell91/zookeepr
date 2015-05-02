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

2. Create the database (*please change the password to something suitably random in the below commands*)
    ```
    sudo -u postgres createuser --no-createdb --no-createrole --no-superuser zookeepr
    sudo -u postgres createdb -O zookeepr zk
    sudo -u postgres psql --command "ALTER USER zookeepr with PASSWORD 'zookeepr'"
    ```

3. Login to the zookeepr user and pull down the git repo and prepare the environment
The following commands should be run in the directory where it is desired to run Zookeepr from (for example: /home/zookeepr/zookeepr or /var/www/zookeepr)
    ```
    sudo -u zookeepr -i
    git clone https://github.com/zookeepr/zookeepr.git
    cd zookeepr/
    virtualenv env --no-site-packages
    . ./env/bin/activate
    exit
    ```

4. Prepare the config files
The following command should be run in the directory where it is desired to store the Zookeepr config files (for example: /home/zookeepr/config)
    ```
    sudo -u zookeepr
    mkdir /home/zookeepr/config
    ch /home/zookeepr/config
    git clone $_some_secret_repo
    ln -s /home/zookeepr/config/lca_info.py /home/zookeepr/zookeepr/zkpylons/config/lca_info.py
    ln -s /home/zookeepr/config/development.ini /home/zookeepr/zookeepr/development.ini
    ```

5. Prepare Zookeepr to run
    ```
    sudo -u zookeepr
    python setup.py develop
    git cherry-pick 7631b73ea4c6df7d219ba1758a72ea779664e8b6
    alembic --config development.ini upgrade head
    git reset --hard HEAD^
    ```

