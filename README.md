# egomedia-django

This is the repository for the egomedia project at [Kings Digital Lab](https://kdl.kcl.ac.uk)

This project uses the technologies outlined in our [Technology Stack](https://stackshare.io/kings-digital-lab/django) and is configured to use [Vagrant](https://www.vagrantup.com/) for local development and [Fabric](http://www.fabfile.org/) for deployment.

## Release notes

### 0.0.4

* Fixed dropdown menus functionality
* Fixed nested modals

### 0.0.3

* Added dropdown menus
* Removed testing tags

### 0.0.2

* Added error page templates

### 0.0.1

First minor release.

* Cards
* Content blocks
* Fixed Font Awesome Pro 5 issue
* Initial styling
* Page types

## Getting started
1. Enter the project directory: `cd egomedia-django`
2. Start the virtual machine: `vagrant up`
3. SSH into the virtual machine: `vagrant ssh`
4. Run the local development server: `./manage.py runserver 0:8000`

You can then access the site locally at [http://localhost:8000](http://localhost:8000)

If the project is ldap-enabled, you can login using your LDAP credentials. Note: LDAP authentication will only work within the college firewall. Alternatively, use the default superuser login:

username: `vagrant`
password: `vagrant`

Note: This login will only work on a locally deployed virtual machine.

## Requirements
* Ansible >= 2.3
* NodeJS
* Vagrant >= 1.9
* VirtualBox >= 5.0
