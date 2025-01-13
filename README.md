# ddvc-hackathon-2025
Code for the Data Driven VC Hackathon 2025 in Paris

# DEAL SOURCING AND SCREENING

This project was built as part of the Data-Driven VC Hackathon organized by [Red River West](https://redriverwest.com) & [Bivwak! by BNP Paribas](https://bivwak.bnpparibas/)

Used to organise unstructured data to structured data, which is then filtered for the purposes of being matched with specific funds. 

## Installation

## Documentation
The project uses an existing API project called Smarty, which receives data from various forms and returns a JSON array. This data includes items on a startup such as pitch decks, urls, and more. From this JSON array, the OpenAI API is called to aid with ranking an investment opportunity's score with various funds, representing the extent in which it matches with that fund.

Inputs:
- mandatory: a data schema in JSON format
- optional: a company pitch deck in PDF format
- optional: a URL
- optional: a user input string (can be a text, random informations, etc.) at least one of the 3 optional inputs must be provided because these are the 3 potential data sources that will be exploited by the AI.

Outputs: 
A JSON schema which includes:
- a summary of the startup, containing information on the fund such as fund name, founders, a description on the fund, etc.
- a ranked list of funds in descending order, from the highest score (highest match) to lowest score (lowest match), with justifications for the scores, along with the categorisation of that fund (e.g. Perfect Match, Likely Match, etc.)

Example of output:
```json
```