import sys
sys.path.append('../')

from  crawler import process_url, split_name, get_image_list

def test_split_name():
    test_string = "https://meteoro.com/content/c/o/ionize/1000/ionize"
    expecetd_result = "ionize"
    assert split_name(test_string) == expecetd_result

def test_process_url():
    test_url = "https://meteoro.com/content/c/o/ionize/1000/ionize"
    test_number = 250    
    expected_result = "https://meteoro.com/content/c/o/ionize/1000/ionize_0250.jpg"
    assert process_url(test_number, test_url) == expected_result
    test_number = 10    
    expected_result = "https://meteoro.com/content/c/o/ionize/1000/ionize_0010.jpg"
    assert process_url(test_number, test_url) == expected_result
    test_number = 9    
    expected_result = "https://meteoro.com/content/c/o/ionize/1000/ionize_0009.jpg"
    assert process_url(test_number, test_url) == expected_result

def test_get_image_list():
    expeceted_test_list = ["https://meteoro.com/content/c/o/ionize/1000/ionize_0001.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0002.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0003.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0004.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0005.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0006.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0007.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0008.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0009.jpg",
    "https://meteoro.com/content/c/o/ionize/1000/ionize_0010.jpg",    
    ]
    assert get_image_list("https://meteoro.com/content/c/o/ionize/1000/ionize", 10) == expeceted_test_list