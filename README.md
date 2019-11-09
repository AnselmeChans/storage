# storage
Package python permettant d’enregistrer et consulter des évènements liés à des dates.

## Description

Un package python permettant d’enregistrer et consulter des évènements liés à des dates.
Ce package est destiné à être utilisé et maintenu par d’autres développeurs de l’équipe. Le
package doit implémenter une classe ​ DatetimeEventStore​ ayant deux méthodes
principales:
    ● DatetimeEventStore.store_event(at, event)​​ permettant de stocker un
    évènement en l’associant à un ​ datetime.datetime​​ .
    ● DatetimeEventStore.get_events(start, end)​​ permettant de récupérer les
    évènements associés aux datetimes appartenant à la période spécifié en paramètre.

## download and install

1. Under the repository name, click to copy the clone URL for the repository. ![](https://github.com/AnselmeChans/storage.git)

2. Clone your project : Go to your cumputer's shell and type the following command: `git clone < Paste HTTPS OR SSH Here > `

2. Go to the location where you want the cloned directory to be made:  `cd <PathWhereIWantToClone_storage>`

3. To easily install Python packages : `sudo python3 setup.py install`

## development

Two prinicpal file :
-   The file store.py contain the class DatetimeEventStore with all the methods
-   the file test contain the main code to test if the package works

# Running the tests

Go to the location where the test file are located : `python3 test.py `

# executable
pip3 install datetime

from storage import DatetimeEventStore
store = DatetimeEventStore()

store.store_event(at, event)
store.get_events(start, end)
store.store_event_csv(self, at, data)
store.get_event_csv(self, start, end)

