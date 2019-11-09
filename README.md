# storage
Python package to record and view events related to dates.

## Description

A python package to record and view events related to dates.
This package is intended to be used and maintained by other team developers. The
package must implement a DatetimeEventStore class that has two main methods:

    ● DatetimeEventStore.store_event (at, event) to store a event by associating it with a datetime.datetime.
    ● DatetimeEventStore.get_events (start, end) to retrieve the events associated with datetimes belonging to the period specified in parameter.

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

