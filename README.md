# User Profile Dashboard Project | [DEMO SITE](https://hack-user-profiles.netlify.app/)

## TABLE OF CONTENTS
- [GET STARTED](#get-started)
- [Project Collaboration Requirements](#project-collaboration-requirements)
- [Phase 1: Basic Profile Cards with Favorite Button](#phase-1-basic-profile-cards-with-favorite-button)
- [Phase 2: Add Modal for User Details and Favorites Column](#phase-2-add-modal-for-user-details-and-favorites-column)
- [Phase 3: Dark Mode Toggle](#phase-3-dark-mode-toggle)
- [Phase 4: Filtering by Country and Name](#phase-4-filtering-by-country-and-name)

> **NOTE**: Each phase builds on the previous one. Start with Phase 1 and progress sequentially.
>
> Each phase is carefully broken down to support beginner developers in learning React. Please proceed phase-by-phase, completing each ticket collaboratively for best learning outcomes.

---

## Get Started

- Clone the repo
- Run the following in the terminal
```bash
npm i
npm run prepare
```

### Instructions for Setting Up GitHub Project Board

We are going to programatically setup your project board using the [project.py](/scripts/project.py) file located in the `/scripts` directory

#### Step 1: Get Your GitHub Personal Access Token (`GITHUB_TOKEN`)
1. Go to GitHub: [GitHub Developer Settings](https://github.com/settings/tokens).
2. Generate a new token with `repo` and `project` permissions.
3. Copy the token and store it securely.

---

#### Step 2: Add GitHub Personal Access Token to Secrets

1. Go to your repository on GitHub.
1. Navigate to Settings > Secrets and variables > Actions.
1. Click on New repository secret.
1. Name the secret GH_TOKEN and paste in your token value, then save.

---

#### Step 3: Update the Script

1. Navigate to the `.github/workflows/setup-board.yml` file to see the GitHub Actions setup.
2. Ensure the following variables are set:
   - REPO: Repository name, e.g., "Repped-School/hack-user-profiles".
   - BOARD_NAME: Name of the project board.

---

#### Step 4: Push the changes to Github
1. Add, commit and push up the changes
1. Merge to the main branch

---

#### Step 5: Run the Action

1. Go to your repository on GitHub.
1. Click on the Actions tab at the top of the repository page.
1. Select the workflow you want to run (in this case, likely "Setup Project Board").
1. Look for the "Run workflow" button on the right side of the workflow screen.
1. Click the Run workflow button. If there are any input fields required, fill them out, then confirm.

---

## Project Collaboration Requirements

- **Create a Repo**: Use the green "Use this template" button to create a repo from this template. **Do NOT fork.**
- **Work Together**: The team should move through each phase together. One person drives while others assist, then rotate!
- **Ticket Time Limit**: Limit each ticket to 10 minutes. If stuck, seek help.
- **Set a Goal Phase**: Decide as a team which phase you aim to complete and post this decision in the designated Slack channel. This goal will set your judging criteria.
- **Collaborative Mindset**: Take turns coding and reviewing. Help each team member stay up to speed.

---

## Phase 1: Basic Profile Cards with Favorite Button

<img width="1421" alt="Screenshot 2024-10-11 at 7 40 09 AM" src="https://github.com/user-attachments/assets/e56a9e2e-d3d2-4a3e-a573-b9337be5f9d7">


### Objective
Display user profile cards with basic details (name, country). Users can hide/show details on each card and favorite a profile.

### Expectations
- Display user profile cards with picture, name, and country.
- A button to toggle additional details (email and phone) on the card.
- A favorite button that visually changes when favorited.

### MVP Tickets (Phase 1)

1. **Setup Repository and Project Board**
   - **User Story**: As a team member, I want a Git repository and project board to collaboratively track and manage our progress.
   - **Acceptance Criteria**: 
     - Repository is created on GitHub, with access provided to all team members, and an initialized README file.
     - Project board is set up using the provided [setup script].
     - Script runs successfully, populating the board with all necessary columns and tickets for each phase.

2. **Fetch and Display User Profiles**
   - **User Story**: As a user, I want to see user profiles on the page.
   - **Acceptance Criteria**: 
       - Fetch 8 user profiles from the Random User API.
       - https://randomuser.me/api/?results=8 _**(to modify number of results, change the query param value)**_
       - Each profile card displays the user’s picture, name, and country.

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
<img width="1377" alt="Screenshot 2024-10-11 at 7 40 19 AM" src="https://github.com/user-attachments/assets/4b1935d4-c847-42a7-a57c-c56d94db9350">


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

https://github.com/user-attachments/assets/304b830b-0497-44f6-aa22-3d3a4599f6ca


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
https://github.com/user-attachments/assets/884c32a9-7375-46df-aabb-9bb88d66f7bd

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
