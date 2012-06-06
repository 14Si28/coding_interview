"""
Given an HTTP server access log file containing IP addresses and dates, extract the unique set of IP addresses within a date range.
"""

import re
import datetime
import unittest
import StringIO

TIMESTAMP_RE = re.compile(r'[0-9]{1,2}/[a-zA-Z]+/[0-9]{4}')
# ipv4 address: 127.0.0.1
IPV4_ADDRESS_RE = re.compile(r'(([0-9]){1,3}\.){3}([0-9]){1,3}')
# ipv6 address examples: 
# Full:                         2001:0db8:85a3:0000:0000:8a2e:0370:7334
# 0's collapsed to ::           2001:db8:85a3::8a2e:370:7334
# ipv4 address as ipv6:         ::ffff:192.0.2.128
# localhost is:                 ::1 
# TODO Handle ipv6 addresses. Note that the regexp becomes nasty to handle all cases.
#IPV6_ADDRESS_RE = re.compile(r'([a-fA-F0-9]):......')

def _parse_time(timestr):
    """
    timestr: format 12/May/2012

    returns: a datetime for timestr
    """
    try:
        return datetime.datetime.strptime(timestr, '%d/%b/%Y')
    except Exception as ex:
        # TODO Logging of original exception (and trace)
        raise Exception('Failed to parse timestamp: {}   Cause: {}'.format(timestr, ex))

def _extract_ip_address(line):
    if not line:
        return None

    ip_address = None
    match = re.search(IPV4_ADDRESS_RE, line)
    if match:
        ip_address = match.group(0)

    return ip_address

def _extract_date(line):
    if not line:
        return None

    when = None
    match = re.search(TIMESTAMP_RE, line)
    if match:
        when = _parse_time(match.group(0))

    return when

def parse_log(logstream):
    ip_data = {}
    for line in logstream:
        ip = _extract_ip_address(line)
        if ip:
            when = _extract_date(line)
            ip_data.setdefault(when, set()).add(ip)

    return ip_data


###########################
# Normally these tests would be in a separate file.
#

TEST_DATE_MAY12 = datetime.datetime(2012, 5, 12, 0, 0)

# Example access log snippet from nginx.
TEST_LOG_SHORT1 = """
127.0.0.1 - - [12/May/2012:22:53:09 -0700] "GET / HTTP/1.1" 200 1168 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19" 
127.0.0.1 - - [12/May/2012:22:53:09 -0700] "GET /static/css/thirdparty/reset.css HTTP/1.1" 200 639 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19" 
1.3.5.7 - - [12/May/2012:22:53:09 -0700] "GET /static/css/base.css HTTP/1.1" 200 501 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19" 
11.10.9.8 - - [13/May/2012:22:53:09 -0700] "GET /static/css/footer.css HTTP/1.1" 200 536 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19" 
127.127.127.127 - - [14/May/2012:22:53:09 -0700] "GET /static/css/splash.css HTTP/1.1" 200 756 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
"""
EXPECTED_SHORT1 = {
    TEST_DATE_MAY12: set(['127.0.0.1', '1.3.5.7']),
    datetime.datetime(2012, 5, 13, 0, 0): set(['11.10.9.8']),
    datetime.datetime(2012, 5, 14, 0, 0): set(['127.127.127.127']),
}

TEST_LOG_REPEATED_ADDR = """
Hidden a bit 38.32.1.99 - - [12/May/2012:22:53:09 -0700] "GET / HTTP/1.1" 200 1168 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19" 
33.32.31.1 - - [12/May/2012:22:53:09 -0700] "GET /127.0.0.1 HTTP/1.1" 200 1168 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19" 
"""
EXPECTED_REPEATED_ADDR = {
    TEST_DATE_MAY12: set(['38.32.1.99', '33.32.31.1'])
}

def str_stream(thestr):
    return StringIO.StringIO(thestr)

class TestAuxiliaryParsers(unittest.TestCase):
    def test_extract_date(self):
        actual = _extract_date('127.0.0.1 - - [12/May/2012:22:53:09 -0700] "GET / HTTP/1.1"')
        self.assertEqual(TEST_DATE_MAY12, actual)

    def test_parse_time(self):
        self.assertEqual(TEST_DATE_MAY12, _parse_time('12/May/2012'))
        self.assertEqual(datetime.datetime(2001, 1, 1, 0, 0), _parse_time('1/Jan/2001'))
        self.assertEqual(datetime.datetime(2001, 1, 1, 0, 0), _parse_time('01/Jan/2001'))
        self.assertEqual(datetime.datetime(2024, 12, 31, 0, 0), _parse_time('31/Dec/2024'))

class TestIPParser(unittest.TestCase):
    def test_parse_short1(self):
        actual = parse_log(str_stream(TEST_LOG_SHORT1))
        self.assertEqual(EXPECTED_SHORT1, actual)

    def test_parse_repeated_address(self):
        actual = parse_log(str_stream(TEST_LOG_REPEATED_ADDR))
        self.assertEqual(EXPECTED_REPEATED_ADDR, actual)

if __name__ == '__main__':
    print parse_log(str_stream(TEST_LOG_SHORT1))

    unittest.main()

