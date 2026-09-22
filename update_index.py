import re

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # SEO
    html = html.replace('Wassim Chouayakh — 1st year engineering student at INSAT Tunisia, specializing in software development and embedded systems (STM32, C/C++, React, Flutter).', 'Wassim Chouayakh — Engineering student at INSAT Tunisia, specializing in full-stack development (React, NestJS) and embedded systems (STM32, CAN/UDS, FreeRTOS).')

    # NavBar CV links
    old_nav_cv = '''<a class="p-2 text-outline hover:text-primary transition-colors" href="CV.pdf"
                        download="CV_Wassim.pdf" title="Télécharger mon CV">
                        <span class="material-symbols-outlined" data-icon="link">link</span>
                    </a>'''
    new_nav_cv = '''<a class="p-2 text-outline hover:text-primary transition-colors" href="ChouayakhWassim.pdf"
                        download="Wassim_Software_CV.pdf" title="Download Software CV">
                        <span class="material-symbols-outlined" data-icon="description">description</span>
                    </a>
                    <a class="p-2 text-outline hover:text-primary transition-colors" href="CV.pdf"
                        download="Wassim_Embedded_CV.pdf" title="Download Embedded CV">
                        <span class="material-symbols-outlined" data-icon="memory">memory</span>
                    </a>'''
    html = html.replace(old_nav_cv, new_nav_cv)

    # Hero Description
    old_hero_desc = '''From code to electronics: I transform ideas into concrete solutions. Specializing in
                        high-performance firmware and robust software architecture.'''
    new_hero_desc = '''From register-level firmware to full-stack web platforms — I transform complex challenges into elegant, high-performance solutions. Bridging the gap between hardware and software, one project at a time.'''
    html = html.replace(old_hero_desc, new_hero_desc)

    # About Me
    old_about_1 = '''Motivated first-year engineering student, passionate about software development and embedded
                        systems. I have already carried out several personal and academic projects with STM32 and
                        various programming languages.'''
    new_about_1 = '''Versatile engineering student with a rare dual expertise in embedded firmware and full-stack software development. At INSAT Tunisia, I've gone far beyond the classroom — designing automotive diagnostic stacks in C, building AI-powered web platforms with React and NestJS, and developing cross-platform mobile applications from scratch.'''
    html = html.replace(old_about_1, new_about_1)

    old_about_2 = '''Curious, rigorous and always ready to learn new technologies. My approach blends the technical
                        rigor of engineering with the creative problem-solving of software development.'''
    new_about_2 = '''What sets me apart is my ability to operate across the entire technology stack: from writing bare-metal register drivers on STM32 microcontrollers to deploying intelligent applications powered by machine learning. This end-to-end perspective allows me to architect solutions that are not just functional, but optimized at every layer.'''
    html = html.replace(old_about_2, new_about_2)

    # Experience
    old_kpit = '''Developed a desktop tool (Flutter + Python backend) to automate Python code analysis for automotive software teams. Features automated formatting with Black & Flake8, customizable rule sets, advanced filtering, and Excel report generation.'''
    new_kpit = '''Designed and developed a cross-platform desktop application (Flutter + Python backend) to automate static code analysis for automotive software teams. The tool enforces coding standards critical for safety-certified codebases — featuring Black & Flake8 integration, customizable rule engines, real-time filtering, and one-click Excel report generation, significantly reducing manual review time.'''
    html = html.replace(old_kpit, new_kpit)

    # Project: Fajri
    old_fajri = '''Simple and minimalist Android app for prayer times, focusing on accurate Fajr (dawn) alerts and daily Islamic prayer schedule. Features include dynamic prayer times calculation, geolocation, local notifications, and persistent background alarms.'''
    new_fajri = '''Cross-platform mobile application engineered for precision — delivering accurate Fajr (dawn) alerts with geolocation-aware prayer time calculations. Built with Flutter, featuring persistent background alarms, local push notifications, and a clean minimalist UI designed for daily reliability.'''
    html = html.replace(old_fajri, new_fajri)

    # Project: Hospital
    old_hospital = '''Full-stack hospital management platform with a multi-tenant architecture. Built with a monorepo approach, it includes JWT authentication, logical tenant-scoped access control, and an integrated Machine Learning model (Python runtime) for patient risk prediction.'''
    new_hospital = '''Enterprise-grade hospital management platform built on a multi-tenant monorepo architecture. Features JWT-authenticated role-based access control, tenant-scoped data isolation, and an integrated Python ML pipeline for real-time patient risk prediction — all served through a modern React 19 frontend backed by NestJS and PostgreSQL.'''
    html = html.replace(old_hospital, new_hospital)

    # Project: SightLine
    old_sight = '''Visual risk analysis platform powered by AI. Analyzes workplace images with risk scoring, compliance recommendations (OSHA, INRS, ISO 45001), and provides a RAG-based assistant for safety questions. Built with React 19, Express backend, PostgreSQL, Prisma ORM, and Google Gemini AI with structured logging and error tracking.'''
    new_sight = '''AI-driven workplace safety platform that transforms visual inspections into actionable intelligence. Upload site photos for automated risk scoring against OSHA, INRS, and ISO 45001 standards. Powered by Google Gemini with structured output, a RAG-based safety assistant, and a production-ready stack: React 19, Express, PostgreSQL, and Prisma ORM.'''
    html = html.replace(old_sight, new_sight)

    # Project: FoodWise
    old_food = '''Intelligent food analysis application that helps users understand their meals in real-time. Features AI vision for meal photo scanning, label OCR, allergen detection, and instant nutritional insights.'''
    new_food = '''Smart nutrition companion that leverages Google Gemini's vision capabilities to decode any meal. Point your camera at food or scan packaging labels — get instant allergen detection, detailed macro/micronutrient breakdowns, and personalized dietary insights. Built with React 19 and TypeScript for a seamless, responsive experience.'''
    html = html.replace(old_food, new_food)

    # Project: KPIT
    old_kpit_proj = '''A powerful desktop application integrating a Flutter frontend with a Python backend. Designed to streamline Python code analysis, it features automated formatting (Black & Flake8), customizable rule imports, advanced filtering, and automated Excel report generation.'''
    new_kpit_proj = '''Professional-grade desktop tool built during my KPIT Technologies internship. Automates Python code quality enforcement for automotive teams — integrating Black formatter, Flake8 linter, custom rule engines, and one-click Excel report generation. Cross-platform Flutter UI communicates with a Python analysis backend.'''
    html = html.replace(old_kpit_proj, new_kpit_proj)

    # Project: VECU-UDS
    old_vecu = '''A C implementation of a Unified Diagnostic Services (UDS) stack and CAN/ISO-TP utilities. Designed for automotive diagnostics, testing, and controlling communications on a CAN network, complete with virtual CAN environment support.'''
    new_vecu = '''Production-quality implementation of the Unified Diagnostic Services (UDS) protocol stack in pure C, targeting automotive ECU diagnostics. Features complete ISO-TP transport layer handling, CAN bus communication management, and a virtual CAN testing environment — built with modular architecture and CMake for cross-platform compilation.'''
    html = html.replace(old_vecu, new_vecu)

    # Project: STM32 Mini
    old_stm = '''A progressive collection of firmware projects for the STM32F103C8T6 (Blue Pill), covering essential peripherals (GPIO, Timers, PWM, UART, ADC, I2C). Features side-by-side implementations using both the STM32 HAL library and bare-metal register programming.'''
    new_stm = '''Comprehensive firmware portfolio demonstrating mastery of the STM32F103C8T6 (Blue Pill) ecosystem. Each project provides dual implementations: one using the HAL abstraction layer and one at the bare-metal register level — covering GPIO, Timers, PWM, UART, ADC, and I2C peripherals. A progressive learning path from blinking LEDs to complex communication protocols.'''
    html = html.replace(old_stm, new_stm)

    # Project: IoT Sensor
    old_iot = '''A real-time environmental monitoring system leveraging an STM32F4 microcontroller and an ESP8266 Wi-Fi module. The firmware features custom ESP8266 drivers via AT commands, efficient UART data reception using DMA (ReceiveToIdle), 12-bit ADC sensor readings, and periodic HTTP data logging to the ThingSpeak API.'''
    new_iot = '''End-to-end IoT pipeline built from scratch: an STM32F4 microcontroller reads environmental sensors via 12-bit ADC, processes data in real-time, and transmits to the cloud through a custom ESP8266 Wi-Fi driver. Features efficient DMA-based UART reception (ReceiveToIdle), AT command protocol handling, and automated HTTP logging to the ThingSpeak analytics platform.'''
    html = html.replace(old_iot, new_iot)

    # Contact Description
    old_contact = '''Ready to collaborate on the next technical breakthrough? Send
                        me a message or find me on professional networks.'''
    new_contact = '''Open to internship opportunities, collaborative projects, and technical
                        challenges across software and embedded systems. Whether you need a
                        full-stack developer, a firmware engineer, or someone who bridges both
                        worlds — let's connect.'''
    html = html.replace(old_contact, new_contact)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print('Update successful')
except Exception as e:
    print('Error:', e)
