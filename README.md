<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Grantimatter/DisBotGPT-Py">
    <img src="./logo.png" alt="Logo" width="160" height="160" style="border-radius:2rem">
  </a>

<h3 align="center">DisBotGPT-PY</h3>

  <p align="center">
    DisBotGPT-PY is a project to bring ChatGPT conversations into discord servers!
    Simply mention the bot in a text channel and the bot will start a new thread with a uniquely generated title! All replies to the bot in these threads will continue these threads.
    <br />
    <a href="https://github.com/Grantimatter/DisBotGPT-Py"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Grantimatter/DisBotGPT-Py/issues">Report Bug</a>
    ·
    <a href="https://github.com/Grantimatter/DisBotGPT-Py/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
---
![DisBotGPT-PY Screen Shot](/example.png)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
---
### Prerequisites

* [Python 3](https://www.python.org/downloads/)

### Installation
1. Clone the repository by running the following command:

    `git clone https://github.com/Grantimatter/DisBotGPT-Py.git`

2. Navigate to the project directory:

    `cd DisBotGPT-Py`

3. Install the required dependencies:

    `pip install -r requirements.txt`

4. Run `main.py`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Bot setup
Setting up a Discord Bot

1. Create a Discord account, if you don't already have one.

2. Go to the [Discord Developers Portal](https://discord.com/developers/docs/game-sdk/applications) and sign in with your Discord account.

3. Click on the "New Application" button.

4. Enter a name for your bot and click on the "Create" button.

5. Go to the "Bot" tab and click on the "Add Bot" button.

6. Click on the "Copy" button next to the "Token" field to copy the bot token. This will be used to authenticate the bot with Discord.

7. Go to the "OAuth2->Url Generator" tab and select the "bot" scope.

8. Under "Bot Permissions", select at least these permissions:
   - Read Messages/View Channels
   - Send Messages
   - Create Public Threads
   - Read Message History

9.  Click on the "Copy" button next to the generated OAuth2 URL and paste it into your browser to add the bot to your Discord server.

## Usage
---
- On first run, the bot will ask for configuration details to get setup.
- Once the configuration is complete and the bot successfully logs in, you should see the bot come online in your discord server.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
---
- [x] Bot will create new conversations (threads) when mentioned with ChatGPT-generated titles
- [x] Bot will remember and continue conversations from each thread

See the [open issues](https://github.com/Grantimatter/DisBotGPT-Py/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
---
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License
---
Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
---
Grant Wiswell - [@grantimattter](https://twitter.com/grantimattter) - wiswellgrant@gmail.com

Project Link: [https://github.com/Grantimatter/DisBotGPT-Py](https://github.com/Grantimatter/DisBotGPT-Py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
---
* [PyCord](https://docs.pycord.dev/en/stable/)
* [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Grantimatter/DisBotGPT-Py.svg?style=for-the-badge
[contributors-url]: https://github.com/Grantimatter/DisBotGPT-Py/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Grantimatter/DisBotGPT-Py.svg?style=for-the-badge
[forks-url]: https://github.com/Grantimatter/DisBotGPT-Py/network/members
[stars-shield]: https://img.shields.io/github/stars/Grantimatter/DisBotGPT-Py.svg?style=for-the-badge
[stars-url]: https://github.com/Grantimatter/DisBotGPT-Py/stargazers
[issues-shield]: https://img.shields.io/github/issues/Grantimatter/DisBotGPT-Py.svg?style=for-the-badge
[issues-url]: https://github.com/Grantimatter/DisBotGPT-Py/issues
[license-shield]: https://img.shields.io/github/license/Grantimatter/DisBotGPT-Py.svg?style=for-the-badge
[license-url]: https://github.com/Grantimatter/DisBotGPT-Py/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png