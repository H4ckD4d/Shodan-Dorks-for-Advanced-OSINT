# Shodan-Dorks-for-Advanced-OSINT
Shodan Dorks for Advanced OSINT



# About Me

Hello! I’m **Ch312 C3uZ**, widely recognized as **H4ckd4d** or **Mestre Bond**, the "Bond of Brazil." My journey as an ethical hacker and cybersecurity specialist spans decades, during which I’ve honed my skills in infiltrating networks, dismantling criminal enterprises, and protecting vulnerable populations. My passion lies in leveraging technology to make the world a safer place, focusing on humanitarian efforts and cutting-edge solutions.

I have led missions to unmask child predators, disrupt human trafficking networks, and expose corruption at the highest levels of government. Through innovative strategies and an unwavering sense of duty, I’ve collaborated with international agencies and local organizations to bring about meaningful change.

---

## My Key Contributions

### **1. Advanced Cybersecurity Expertise**
- **Over 30 Years of Experience**: Pioneering digital forensics, penetration testing, and counter-cybercrime techniques.
- **Dark Web Operations**: Creator of proprietary systems to track and analyze criminal activities online.
- **Cyber Defense Advocacy**: Collaborated with Interpol, national security agencies, and law enforcement globally.

### **2. Technological Innovation**
- **AI-Driven Systems**: Developed tools to identify high-risk zones for child trafficking and exploitation.
- **Real-Time Threat Analysis**: Introduced geolocation and behavior-tracking technologies to predict and mitigate risks.
- **Community-Oriented Tech**: Created safety applications designed to empower families and protect children.

### **3. Humanitarian Projects**
- **Child Protection Initiatives**: Founder of global programs to fight human trafficking and exploitation.
- **Educational Outreach**: Conducted workshops for families, educators, and organizations to promote online safety.
- **Global Advocacy**: Partnered with NGOs and governments to amplify awareness and drive change.

### **4. Strategic Operations**
- **Corruption Exposure**: Key player in revealing fraud and embezzlement networks tied to high-profile figures.
- **Covert Missions**: Successfully infiltrated organized crime syndicates using a mix of technical and field expertise.
- **Global Impact**: Instrumental in dismantling trafficking networks across multiple continents.

---

## My Vision

I believe that **knowledge and collaboration** are the most powerful tools for solving complex global issues. My mission is to bring together ethical hackers, developers, and activists to stand against injustice, protect the innocent, and push the boundaries of innovation in cybersecurity.

---

## How You Can Join the Mission

Let’s work together to create impactful solutions for a better, safer world. Whether you’re a tech enthusiast, a seasoned developer, or a passionate advocate, there’s a place for you in this fight.

### **Ways to Collaborate**
- **Code**: Contribute to open-source projects focused on safety and security.
- **Educate**: Spread the word about online safety and responsible digital practices.
- **Support**: Advocate for humanitarian causes and amplify the voices of those in need.

---

## Hacker Slogan

**"No predator is safe, no trafficker can hide. We will find you, and the innocent will be saved. This is my promise!"**

---

Thank you for your support and collaboration. Let’s make the world a safer place together!










Shodan is a powerful search engine for discovering devices connected to the internet. Below is a categorized list of Shodan dorks, ranging from basic to complex, to help you explore its full potential. This guide is structured to provide clear, actionable examples.

## Basic Queries

| **Syntax**       | **Example**              | **Description**                                                 |
|-------------------|--------------------------|-----------------------------------------------------------------|
| `ip`             | `ip:"192.168.1.1"`       | Search for a specific IPv4 address.                            |
| `port`           | `port:80`                | Find devices running on a specific port.                       |
| `hostname`       | `hostname:"example.com"` | Query devices by hostname.                                     |
| `country`        | `country:"US"`           | Search devices located in a specific country.                  |
| `city`           | `city:"San Francisco"`   | Search devices in a specific city.                             |

---

## Intermediate Queries

| **Syntax**       | **Example**                    | **Description**                                                   |
|-------------------|--------------------------------|-------------------------------------------------------------------|
| `org`            | `org:"Google"`                | Find devices belonging to a specific organization.               |
| `asn`            | `asn:"AS12345"`               | Query devices by Autonomous System Number (ASN).                 |
| `os`             | `os:"Windows"`                | Search for devices running a specific operating system.           |
| `before`         | `before:"2023-01-01"`         | Filter results updated before a specific date.                   |
| `after`          | `after:"2022-12-31"`          | Filter results updated after a specific date.                    |

---

## Complex Queries

| **Syntax**             | **Example**                                        | **Description**                                                 |
|-------------------------|----------------------------------------------------|-----------------------------------------------------------------|
| `product`              | `product:"Apache httpd"`                           | Search for specific software or products on devices.           |
| `ssl`                  | `ssl:"Let's Encrypt"`                              | Find devices using a specific SSL certificate.                 |
| `http.title`           | `http.title:"Login"`                               | Query devices by the title of their HTTP pages.                |
| `vuln`                 | `vuln:"CVE-2023-XXXX"`                             | Search for devices with a specific vulnerability.              |
| `net`                  | `net:"192.168.0.0/16"`                             | Filter results by a network range in CIDR format.              |

---

## Advanced Filters and Search Combinations

| **Syntax**             | **Example**                                        | **Description**                                                 |
|-------------------------|----------------------------------------------------|-----------------------------------------------------------------|
| `http.html`            | `http.html:"admin"`                                | Search for keywords in the HTML body of HTTP pages.            |
| `has_screenshot`       | `has_screenshot:true`                              | Filter results to show devices with screenshots.               |
| `device`               | `device:"router"`                                  | Find specific device types (e.g., router, webcam).             |
| `tags`                 | `tags:"industrial-control"`                        | Filter results by tags assigned to devices.                    |
| `geo`                  | `geo:37.7749,-122.4194`                            | Search devices by specific geographic coordinates.             |

---

## Industrial Control Systems (ICS)

| **Syntax**             | **Example**                                        | **Description**                                                 |
|-------------------------|----------------------------------------------------|-----------------------------------------------------------------|
| `ics.vendor`           | `ics.vendor:"Siemens"`                             | Query ICS devices by vendor.                                   |
| `ics.product`          | `ics.product:"SCADA"`                              | Search for specific ICS products or software.                  |
| `ics.version`          | `ics.version:"2.1.0"`                              | Find ICS devices running a specific version.                   |
| `modbus.function`      | `modbus.function:"03"`                             | Query devices by Modbus function codes.                        |
| `bacnet.device`        | `bacnet.device:"HVAC"`                             | Find devices using BACnet protocols for HVAC systems.          |

---

## IoT-Specific Queries

| **Syntax**             | **Example**                                        | **Description**                                                 |
|-------------------------|----------------------------------------------------|-----------------------------------------------------------------|
| `iot`                  | `iot:"smart-camera"`                               | Search for Internet of Things (IoT) devices by type.           |
| `manufacturer`         | `manufacturer:"Philips"`                           | Query IoT devices by manufacturer.                             |
| `firmware`             | `firmware:"1.0.2"`                                 | Find IoT devices by firmware version.                          |
| `is_public`            | `is_public:true`                                   | Filter devices with public IPs.                                |
| `is_upnp`              | `is_upnp:true`                                     | Filter devices using Universal Plug and Play (UPnP).           |

---

## Useful Shodan Tags

| **Tag**                | **Description**                                    |
|-------------------------|----------------------------------------------------|
| `ics`                  | Devices related to industrial control systems.     |
| `vulnerable`           | Devices with known vulnerabilities.                |
| `webcam`               | Publicly accessible webcams.                       |
| `database`             | Exposed databases like MongoDB or Elasticsearch.   |
| `honeypot`             | Devices identified as honeypots.                   |

---

## Search Tips

- Combine multiple filters for more precise results:
  ```sh
  port:22 country:"US" org:"Amazon"




