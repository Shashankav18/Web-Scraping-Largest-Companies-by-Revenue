# 🏢 Web Scraping Project: Largest Companies by Revenue

This project extracts the **list of the world's largest companies by revenue** from a public website (Wikipedia) using **Python, BeautifulSoup, and Pandas**.  
It demonstrates how to automate data extraction, cleaning, and storage using web scraping techniques.

---

## 📊 Project Overview

The goal of this project is to scrape company data such as:
- **Rank**
- **Company Name**
- **Industry**
- **Revenue (in USD Billions)**
- **Headquarters**

The extracted data is then cleaned and saved as a CSV file for further analysis.

---

## ⚙️ Tools & Libraries Used

| Tool | Purpose |
|------|----------|
| **Python 3** | Programming language used |
| **Requests** | To send HTTP requests to fetch HTML content |
| **BeautifulSoup (bs4)** | To parse and extract data from HTML |
| **Pandas** | To structure, clean, and export data into CSV |
| **Jupyter Notebook / VS Code** | For development and testing |

---

## 📂 Folder Structure

```
/largest-companies-by-revenue-scraper
│
├── main.py                         # Python script for scraping and saving data
├── requirements.txt                 # Dependencies used
│
├── data/
│   └── largest_companies.csv        # Final scraped dataset
│
│
├── README.md                        # Documentation
└── LICENSE                          # Optional
```

---

## 🚀 How to Run the Project

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/largest-companies-by-revenue-scraper.git
   cd largest-companies-by-revenue-scraper
   ```

2. **Install required libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**
   ```bash
   python main.py
   ```

4. **View the output**
   - The data will be saved in the folder:  
     `data/largest_companies.csv`

---

## 🖼️ Example Output

![Scraped Output Preview](screenshots/scraped_output_preview.png)

| Rank | Company | Industry | Revenue (USD billions) | Headquarters |
|------|----------|-----------|------------------------|---------------|
| 1 | Walmart | Retail | 611.3 | United States |
| 2 | Saudi Aramco | Oil & Gas | 603.7 | Saudi Arabia |
| 3 | Amazon | E-commerce | 513.9 | United States |
| ... | ... | ... | ... | ... |

---

## 💡 Key Learning Points

- Using `requests` to fetch website HTML content  
- Parsing and extracting HTML table data using `BeautifulSoup`  
- Cleaning and structuring data with `pandas`  
- Exporting data into `.csv` format  
- Following ethical web scraping guidelines (avoiding excessive requests, crediting source)

---

## ⚠️ Ethical Note

This project is for **educational purposes only**.  
Always review a website’s **robots.txt** and **terms of service** before scraping.

---

## 🧑‍💻 Author

**Shashank AV**

---

## 📜 License

This project is open-source and available under the **MIT License**.  
Feel free to use, modify, and share with proper credit.

---

## 🧰 requirements.txt

```text
requests
beautifulsoup4
pandas
```
