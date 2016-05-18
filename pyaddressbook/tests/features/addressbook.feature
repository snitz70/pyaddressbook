# Created by Brian Snyder at 5/17/2016
Feature: Addressbook
  In order to save contacts
  As a user
  We'll start using an addressbook


  Scenario: Add addressbook
    Given I want to use an addressbook
    When I create a new addressbook
    Then I expect the new one to be created

  @wip
  Scenario: Add addressbook if existing
    Given I want to create a new addressbook
    When addressbook already exists
    Then I expect that the addressbook will not get created

  

