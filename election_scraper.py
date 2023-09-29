import sys
import csv
import requests
from bs4 import BeautifulSoup


def fetch_html_content(url):
    """Fetch the HTML content from the provided URL."""
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def extract_towns(html_content):
    """Retrieve a list of towns from the given HTML content."""
    return [td.text for td in html_content.find_all("td", "overflow_name")]


def extract_links(html_content):
    """Extract the detailed URLs for each town's voting results from the given HTML content."""
    base_url = "https://volby.cz/pls/ps2017nss/"
    return [base_url + td.a["href"] for td in html_content.find_all("td", "cislo")]


def extract_ids(html_content):
    """Extract town identification numbers from the given HTML content."""
    return [td.text for td in html_content.find_all("td", "cislo")]


def extract_parties(link):
    """Extract the list of parties from the given link."""
    html_content = fetch_html_content(link)
    return [td.text for td in html_content.find_all("td", "overflow_name")]


def extract_votes_data(link):
    """Extract voting data (voters, attendance, valid votes, and votes per party) from the given link."""
    html_content = fetch_html_content(link)

    voters = html_content.find("td", headers="sa2").text.replace('\xa0', ' ')
    attendance = html_content.find("td", headers="sa3").text.replace('\xa0', ' ')
    valid_votes = html_content.find("td", headers="sa6").text.replace('\xa0', ' ')

    party_votes = [td.text + ' %' for td in html_content.find_all("td", headers=["t1sb4", "t2sb4"])]

    return [voters, attendance, valid_votes] + party_votes


def write_to_csv(file_name, header, content):
    """Write the given header and content to a CSV file."""
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(content)


def main(url, output_filename):
    initial_html_content = fetch_html_content(url)
    print("I am downloading data from URL", url)
    print("I am saving data to file", output_filename)


    towns = extract_towns(initial_html_content)
    links = extract_links(initial_html_content)
    ids = extract_ids(initial_html_content)

    # Extract party names from the first link since it should be consistent across all links
    parties = extract_parties(links[0])
    header = ['Code', 'Location', 'Voters', 'Envelopes', 'Valid votes'] + parties

    # For each link, extract the voting data
    rows = []
    for town_id, town_name, link in zip(ids, towns, links):
        voting_data = extract_votes_data(link)
        row = [town_id, town_name] + voting_data
        rows.append(row)

    write_to_csv(output_filename, header, rows)



if __name__ == '__main__':
    # Check if the right number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: script_name.py <URL> <output_filename>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
    print("End of election_scraper.py")  # Announce the end of the program

