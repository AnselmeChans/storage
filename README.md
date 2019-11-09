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

## Cas d'utilisation
