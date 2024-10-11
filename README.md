# User Profile Dashboard Project

## TABLE OF CONTENTS
- [Project Collaboration Requirements](#project-collaboration-requirements)
- [Phase 1: Basic Profile Cards with Favorite Button](#phase-1-basic-profile-cards-with-favorite-button)
- [Phase 2: Add Modal for User Details and Favorites Column](#phase-2-add-modal-for-user-details-and-favorites-column)
- [Phase 3: Dark Mode Toggle](#phase-3-dark-mode-toggle)
- [Phase 4: Filtering by Country and Name](#phase-4-filtering-by-country-and-name)

> **NOTE**: Each phase builds on the previous one. Start with Phase 1 and progress sequentially.

---

## Project Collaboration Requirements

- **Create a Repo**: Use the green "Use this template" button to create a repo from this template. **Do NOT fork.**
- **Work Together**: The team should move through each phase together. One person drives while others assist, then rotate!
- **Ticket Time Limit**: Limit each ticket to 10 minutes. If stuck, seek help.
- **Set a Goal Phase**: Decide as a team which phase you aim to complete and post this decision in the designated Slack channel. This goal will set your judging criteria.
- **Collaborative Mindset**: Take turns coding and reviewing. Help each team member stay up to speed.

---

## [DEMO SITE](https://hack-user-profiles.netlify.app/)

---

## Phase 1: Basic Profile Cards with Favorite Button



### Objective
Display user profile cards with basic details (name, country). Users can hide/show details on each card and favorite a profile.

### Expectations
- Display user profile cards with picture, name, and country.
- A button to toggle additional details (email and phone) on the card.
- A favorite button that visually changes when favorited.

### MVP Tickets (Phase 1)

1. **Setup Repository**
   - **User Story**: As a team member, I want a Git repository to track and save our project.
   - **Acceptance Criteria**: Repository is created on GitHub, with access for all team members and an initialized README.

2. **Fetch and Display User Profiles**
   - **User Story**: As a user, I want to see user profiles on the page.
   - **Acceptance Criteria**: Fetch 8 profiles from [Random User API](https://randomuser.me/api/?results=8). Display picture, name, and country on each card.

3. **Add Favorite Button**
   - **User Story**: As a user, I want to mark profiles as favorites.
   - **Acceptance Criteria**: Add a favorite/unfavorite button on each profile card. Favorited profiles change button appearance (e.g., red when favorited).

4. **Toggle User Details on Card**
   - **User Story**: As a user, I want to toggle additional profile details on each card.
   - **Acceptance Criteria**: Clicking a button shows/hides additional details (email, phone).

5. **Phase 1 Documentation**
   - **User Story**: As a team, we want documentation of our work in this phase.
   - **Acceptance Criteria**: README includes Phase 1 explanation and screenshots of the completed phase.

---

## Phase 2: Add Modal for User Details and Favorites Column

### Objective
Replace on-card details toggle with a modal view. Add a favorites column to display favorited profiles.

### Expectations
- A modal displays user details.
- Remove the details toggle on the card.
- Add a "Favorites" column with favorited profiles.
- Add a "View More Profiles" button to fetch new profiles and overwrite the current list.

### MVP Tickets (Phase 2)

1. **Replace Details Toggle with Modal**
   - **User Story**: As a user, I want to view profile details in a modal.
   - **Acceptance Criteria**: Clicking a profile opens a modal with a larger picture, name, email, phone, and location.

2. **Add Favorites Column**
   - **User Story**: As a user, I want a section to view my favorited profiles.
   - **Acceptance Criteria**: Display favorited profiles in a right-side column, each with a smaller card layout.

3. **View More Profiles Button**
   - **User Story**: As a user, I want to refresh the profile list.
   - **Acceptance Criteria**: Button fetches a new set of 8 profiles, overwriting the current list.

4. **Phase 2 Documentation**
   - **User Story**: As a team, we want documentation of our work in this phase.
   - **Acceptance Criteria**: README includes Phase 2 functionality, modal explanation, and screenshots.

---

## Phase 3: Dark Mode Toggle

### Objective
Enhance the user experience with a Dark Mode toggle, allowing users to switch between light and dark themes.

### Expectations
- Add a Dark Mode toggle in the navbar.
- All components adjust colors based on the chosen theme.

### MVP Tickets (Phase 3)

1. **Add Dark Mode Toggle**
   - **User Story**: As a user, I want the option to switch between dark and light themes.
   - **Acceptance Criteria**: Toggle button switches the theme for all components.

2. **Dark Mode Styling**
   - **User Story**: As a user, I want consistent styling for dark and light themes.
   - **Acceptance Criteria**: Cards, modals, and other components adapt styling based on the theme.

3. **Phase 3 Documentation**
   - **User Story**: As a team, we want documentation of our work in this phase.
   - **Acceptance Criteria**: README includes dark mode instructions and screenshots in both themes.

---

## Phase 4: Filtering by Country and Name

### Objective
Add filtering by country and sorting by first or last name to enhance search capabilities.

### Expectations
- Filter dropdown for country (dynamically populated from loaded profiles).
- Sort profiles by first or last name.

### MVP Tickets (Phase 4)

1. **Add Country Filter Dropdown**
   - **User Story**: As a user, I want to filter profiles by country.
   - **Acceptance Criteria**: Dropdown shows countries from loaded profiles. Selecting a country filters displayed profiles.

2. **Sort by First or Last Name**
   - **User Story**: As a user, I want to sort profiles alphabetically.
   - **Acceptance Criteria**: Dropdown allows sorting by first or last name. Profiles reorder based on selection.

3. **Final Documentation**
   - **User Story**: As a team, we want complete documentation of our project.
   - **Acceptance Criteria**: README includes a project overview, final screenshots, and deployment link.

---

Each phase is carefully broken down to support beginner developers in learning React. Please proceed phase-by-phase, completing each ticket collaboratively for best learning outcomes.
