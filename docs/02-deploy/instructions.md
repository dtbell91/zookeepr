# Zookeepr Deployment Instructions
This document details how to deploy a Zookeepr instance with automated deployment from Github.

# Prerequisites
In order to continuously deploy Zookeepr, two separate Git repositories are required:
 - A public repo (e.g. zookeepr/zookeepr); and
 - A private report (for storing the secret config files)

A cron job can then be configured to maintain the Zookeepr code up to the currently desired commit by tags (eg. lca2016-prod or lca2016-uat), likewise for configuration from the private repo.

You should also have a user which admins can sudo into to own your instance's files (e.g. zkconf-zookeepr-prod or zkconf-zookeepr-uat)

# Suggested Folder Structure
This is the suggested folder structure for Zookeepr. Using this standard layout will help keep things consistent across multiple Zookeepr instances (e.g. simultaneous conferences) on the same host.

Replace "zookeepr.conf.au" with the domain for your website.

```
/srv/http/zookeepr.conf.au/log
/srv/http/zookeepr.conf.au/zookeepr
/srv/http/zookeepr.conf.au/zookeepr-config
```

The folders are then used as follows:
 - log contains the apache logs, and should belong to root/www-data/apache user
 - zookeepr contains the Zookeepr code, potentially from your conferences fork/branch. This should belong to your instance's user (e.g. zkconf-zookeepr-prod)
 - zookeepr-config contains your Zookeepr config from your private repo. This should belong to your instance's user (e.g. zkconf-zookeepr-prod)
