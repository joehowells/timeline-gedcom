# timeline-gedcom
Workflow for generating cards for the card game [Timeline](https://www.zygomatic-games.com/en/game/timeline-classic/),
based on family tree data stored in the Genealogical Data Communication (GEDCOM) file format.

Some genealogy websites such as [Ancestry](https://www.ancestry.com/) and [FindMyPast](https://www.findmypast.com/)
let their users export their family trees to GEDCOM format. These users could use this project to create a personalised
deck of Timeline cards from their respective family trees.

The basic idea is to extract all possible events (e.g., births, deaths, marriages) from the GEDCOM file, then select
a subset of these events (say 50) to use as cards. We want our cards to be spread out across the family tree, not
clumped together around a particular date, location or individual. We can achieve this by defining features for the
following pieces of information associated with each event:

- Type (e.g., birth, death or marriage) 
- Date
- Individual(s) involved
- Location

Once we have these features, we can use them to divide the events into clusters with similar feature values. We create
clusters equal to the number of cards we want, and select one event from each cluster to convert to a card.
