# Student Performance Analytics System — Web Edition

A static frontend version of my student analytics project. It uses HTML, CSS and JavaScript and can be deployed directly to Netlify.

## Features
- Dashboard showing student count, class average, attendance and pass rate
- Subject-wise average charts and top 3 performers
- Search students and filter by department or result
- Sort table columns by clicking their headings
- Import a CSV and export a report as CSV

## Deploy on Netlify
1. Download and extract this ZIP.
2. Open Netlify and choose **Add new site → Deploy manually**.
3. Drag the extracted folder containing `index.html` into the deploy area.
4. Open the URL Netlify provides.

No build command is required.

CSV imports need these columns: `name`, `ID`, `DEPT`, `ATDN`, `DS`, `AI`, `ML`, `DL`. Imported data updates the current browser session only; it is not saved to a server.
