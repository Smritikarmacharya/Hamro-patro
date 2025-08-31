
import pytest
from Home_Page import HomePage
from Rashifal_Page import RashifalPage


def test_rashifal_tula_visible(setup):
    #Test case to verify Tula rashi is visible on the Rashifal page
    # Initialize the page objects
    home_page = HomePage(setup)
    rashifal_page = RashifalPage(setup)
    
    # Open the homepage
    home_page.open()
    
    # Click on the Rashifal tab
    home_page.click_rashifal()
    
    # Verify if Tula is visible
    assert rashifal_page.is_tula_visible(), "Tula rashi is not visible!"
