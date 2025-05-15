# Bug Classifier Agent

A multi-agent system for analyzing, classifying, and recommending fixes for software bugs.

## Overview

This agent harnesses the power of multiple specialized sub-agents to process bug reports and provide comprehensive analysis including:

- Bug type classification
- Severity estimation
- Action recommendations
- Summary generation

The multi-agent architecture allows for specialized processing of different aspects of bug analysis, resulting in more accurate and useful outputs.

## Architecture

The system consists of the following sub-agents:

### 1. Bug Type Classifier
Analyzes the bug description and classifies it into one of the following categories:
- UI Bug
- Functionality Bug
- Backend/API Bug
- Security Bug
- Compatibility Bug
- Configuration/Environment Bug
- Data/State Bug
- Logic Bug

### 2. Bug Severity Estimator
Evaluates the impact and urgency of the bug, classifying it as:
- Critical
- High
- Medium
- Low

### 3. Action Recommender
Provides specific, actionable recommendations for addressing the bug based on its type and severity, including:
- Immediate actions
- Testing recommendations
- Prevention measures

### 4. Bug Summary Generator
Creates a comprehensive, well-structured bug report suitable for development teams, containing:
- Bug description
- Steps to reproduce
- Impact analysis
- Environment details
- Recommended actions

## Usage

### Prerequisites
- Google ADK (Agent Development Kit)
- Python 3.9+

### Running the Agent

1. Navigate to the multi-agent directory:
   ```
   cd sequential-agent
   ```

2. Start the ADK web interface:
   ```
   adk web
   ```

3. In the web interface, select the bug-classifier-agent and submit your bug report

### Test Examples

Here are several example bug reports you can use to test the agent:

#### Example 1: UI Bug
```
Bug description: The dropdown menu in the user settings page doesn't display correctly on mobile devices. The menu items overlap and some options are not clickable. This only happens on iOS devices with Safari browser.
```

#### Example 2: Functionality Bug
```
Bug description: When users attempt to submit the payment form with valid credit card information, the system displays a success message but the payment is not processed, resulting in orders showing as 'pending' indefinitely. This happens approximately 40% of the time, regardless of browser or device.
```

#### Example 3: Security Bug
```
Bug description: Users report being able to access other users' account information by modifying the user ID parameter in the URL after logging in. This exposes personal information including names, addresses, and partial credit card numbers. The issue was discovered in the production environment yesterday.
```

#### Example 4: Backend/API Bug
```
Bug description: The product search API is returning a 500 Internal Server Error when search queries contain special characters like "&" or "%". This prevents users from searching for certain products and is affecting approximately 15% of search attempts. Server logs show uncaught exceptions in the query parsing module.
```

#### Example 5: Data/State Bug
```
Bug description: Customer order history is showing duplicate entries for some transactions. After a user completes an order, the same order appears multiple times in their history, though the backend database correctly shows only one transaction. This is causing confusion for customers who think they've been charged multiple times.
```

#### Example 6: Compatibility Bug
```
Bug description: The video conferencing feature works correctly in Chrome and Firefox but fails to initialize in Microsoft Edge. Users on Edge browsers receive a "Camera access denied" error even when they have granted permission. Approximately 20% of our corporate users are affected as they use Edge as their default browser.
```

#### Example 7: Configuration/Environment Bug
```
Bug description: After the recent deployment to the staging environment, all image uploads are failing with a "Storage configuration error" message. The same code works correctly in development and production environments. DevOps team reports no changes to the storage configuration but notes that the staging environment was recently migrated to a new cloud region.
```

#### Example 8: Logic Bug
```
Bug description: The discount calculation for promotional codes is incorrect when a user's cart contains both discounted and regular-priced items. The system applies the discount percentage to the entire cart rather than just the eligible items, resulting in larger discounts than intended. Finance team estimates this is costing approximately $5,000 per week in lost revenue.
```

### Example Output

```
## Bug Summary: Mobile dropdown menu rendering issue in user settings

**Bug ID:** BUG-2023-05-15-001
**Type:** UI Bug
**Severity:** Medium
**Reported:** 2023-05-15
**Status:** New

### Description
The dropdown menu in the user settings page doesn't render correctly on iOS devices with Safari, causing overlapping menu items and making some options unclickable.

### Steps to Reproduce
1. Open the application on an iOS device using Safari
2. Navigate to the user settings page
3. Tap on any dropdown menu
4. Observe the menu layout and attempt to interact with all options

### Expected Behavior
All dropdown menu items should display properly aligned with appropriate spacing and be fully interactive.

### Actual Behavior
Menu items overlap each other and some options cannot be clicked or tapped.

### Impact
- **User Impact:** iOS users cannot access certain settings options, hindering their ability to configure preferences
- **Business Impact:** Potential increase in support tickets and reduced user satisfaction
- **Scope:** Affects approximately 30% of mobile users (iOS Safari users)

### Environment
- iOS 15.0+
- Safari browser
- User settings page

### Recommended Actions
1. Inspect Safari-specific CSS issues in the dropdown component
2. Implement mobile-specific styling for dropdown menus
3. Add iOS-specific testing to the QA process

### Additional Notes
This issue does not appear on Android devices or when using other browsers on iOS.
```

## Extending the Agent

To add new capabilities or modify existing ones:

1. Create or modify sub-agent modules in the respective directories
2. Update the prompt files to refine agent behaviors
3. Modify the main agent code to integrate new sub-agents or features

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 