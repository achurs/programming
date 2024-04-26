#make a program to download the specified courses from mit
#the way this program works is that the user has to enter the name of the course
#the script then downloads the course from mit and saves it in the current directory

from ast import main
from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import tqdm
import wget

def setup_driver(course_code):
    """
    Sets up a webdriver, goes to the MIT OpenCourseWare search page, gets the
    page source and quits the driver. Returns the page source.

    Arguments:
        course_code {str} -- The course code to search for

    Returns:
        str -- The page source of the search page
    """
    driver = webdriver.Chrome()
    #Go to the MIT OpenCourseWare search page
    driver.get(f"https://ocw.mit.edu/search/?q={course_code}")
    #Get the page source
    page_source = driver.page_source
    #Quit the driver
    driver.quit()
    #Return the page source
    return page_source

def get_the_course_website_url(course_code: str) -> str:
    """
    Gets the URL of the course website given the course code

    Args:
        course_code (str): The course code of the course

    Returns:
        str: The URL of the course website
    """
    parsed_html = BeautifulSoup(setup_driver(course_code), "html.parser")
    search_results = parsed_html.find("section", {"aria-label": "OpenCourseWare Search Results"})
    the_useful_result = search_results.find("article",{"aria-labelledby": "search-result-0-title"})  # type: ignore
    the_course_website_url = "https://ocw.mit.edu" + the_useful_result.find("a")["href"]  # type: ignore
    return the_course_website_url

def course_outline(url: str) -> dict:
    """
    Gets the title, instructors, and description of a course given the URL

    Args:
        url (str): The URL of the course website

    Returns:
        dict: A dictionary containing the title, instructors, and description of the course
    """
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    parsed_html = BeautifulSoup(html, "html.parser")
    course_info = {}
    course_info['Title'] = parsed_html.title.text  # type: ignore
    instructors = parsed_html.find_all("a", {"class": "course-info-instructor"})
    course_info['Instructors'] = list(set([instructor.text for instructor in instructors]))
    description = parsed_html.find("div", {"class": "description"})
    if description is not None:
        course_info['Discription'] = description.text.strip()  # type: ignore
    else:
        course_info['Discription'] = ""
    return course_info

def file_links_getter(url: str) -> list[str]:
    """
    Gets all the downloadable links from a given URL

    Args:
        url (str): The URL to get the links from

    Returns:
        List[str]: A list of all the downloadable links from the URL
    """
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    parsed_html = BeautifulSoup(html, "html.parser")
    download_links = parsed_html.find_all("a")  # type: ignore
    links = []
    for link in download_links:
        # Check if the link has a file extension of pdf, zip, or mp4
        if any(extension in link["href"] for extension in [".pdf", ".zip", ".mp4"]):
            links.append(link["href"])
    return links


def downloader(links):
    """
    Downloads all the links using wget

    Args:
        links (List[str]): A list of links to download
    """
    for link in tqdm.tqdm(links):
        # Check if the link is an absolute link or a relative link
        if "https" in link:
            print("Downloading:", link)
            wget.download(link)
        else:
            # If the link is a relative link, add the base URL to it
            print("Downloading:", "https://ocw.mit.edu" + link)
            wget.download("https://ocw.mit.edu" + link)

if __name__ == "__main__":
    code = input("Enter the course code: ")
    url = get_the_course_website_url(code)
    dict = course_outline(url)
    for key, value in dict.items():
        print(key, ":", value)
    download_url = url + "download"
    file_links = file_links_getter(download_url)
    downloader(file_links)