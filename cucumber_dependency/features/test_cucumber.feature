Feature: Hamilton council website

Scenario: Basic Google Search
Given I navigate to "https://www.google.com"
When I search for "Hamilton council"
Then I see "Hamilton council" in the results
Then I click "Hamilton City Council" in the results
Then I click the rubbish link
Then I scroll down
Then I run axe
Then I quit the browser