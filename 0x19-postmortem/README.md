# Postmortem: March 2024 Server Access Lock-Out Incident

## Overview
This postmortem document provides an analysis of the server access lock-out incident that occurred in March 2024. It outlines the duration of the outage, its impact, root cause, timeline of events, resolution, and corrective/preventative measures taken.

## Issue Summary
- **Duration:** March 3, 2024, 10:00 AM SAST to March 5, 2024, 11:30 AM SAST
- **Impact:** Critical access to web-01, web-02 servers, and the ld-01 load balancer was lost, disrupting ongoing configuration tasks and delaying the setup process.
- **Root Cause:** Inadvertent erasure of SSH configuration keys following a reset of the user Docker container.

## Timeline
- **March 3, 2024:**
  - 10:00 AM SAST: Initiated reset of user Docker container, leading to immediate loss of server access.
- **March 4, 2024:**
  - 10:05 AM SAST: Issue escalated to ALX Staff, requesting assistance from Alfred Tuva.
  - 10:15 AM SAST: Alfred Tuva began investigating the root cause.
- **March 5, 2024:**
  - 10:30 AM SAST: Alfred Tuva identified erasure of SSH configuration keys as primary cause.
  - 10:45 AM SAST: SSH keys reconfigured, restoring access to affected servers and load balancer.
  - 11:30 AM SAST: Ongoing configuration tasks resumed.

## Root Cause and Resolution
- **Root Cause:** Inadvertent erasure of SSH configuration keys during Docker container reset.
- **Resolution:** ALX Staff, led by Alfred Tuva, reconfigured SSH keys to restore critical access.

## Corrective and Preventative Measures
- **Improvements/Fixes:**
  - Debugging AirBnB Clone MySQL App.
  - Completion of web-02 Setup.
- **Tasks:**
  - Conduct thorough examination of AirBnB Clone MySQL App.
  - Finalize setup and configuration of web-02.

## Conclusion
This postmortem underscores the importance of robust backup mechanisms and caution during routine system maintenance to prevent inadvertent disruptions. By implementing proactive measures and maintaining vigilant oversight, we aim to minimize the occurrence of such incidents and ensure the stability and reliability of our infrastructure.
