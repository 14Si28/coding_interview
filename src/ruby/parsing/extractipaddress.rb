#!/usr/bin/env ruby
#
# Given an HTTP server access log file containing IP addresses and dates, extract the unique set of IP addresses within a date range.
#

require 'set'
require 'test/unit'
require 'date'

DATE_FORMAT = '%d/%b/%Y'
TIMESTAMP_RE = /[0-9]{1,2}\/[a-zA-Z]+\/[0-9]{4}/
# ipv4 address: 127.0.0.1
IPV4_ADDRESS_RE = /(([0-9]){1,3}\.){3}([0-9]){1,3}/
# Not implementing ipv6 addresses.


class LogParser
  def parse_log(stream)
    ip_data = {}
    stream.each_line do |line|
      ip = extract_match(IPV4_ADDRESS_RE, line)
      if ip
        dt = extract_match(TIMESTAMP_RE, line)
        if dt
          dt = Date.strptime(dt, DATE_FORMAT)
          (ip_data[dt] ||= Set.new) << ip
        end
      end
    end

    ip_data
  end

  private

  def extract_match(regex, from_str)
    match = regex.match(from_str)
    return match[0] if match
    nil
  end
end


###########


TEST_DATE_MAY12 = Date.new(2012, 5, 12)

# Example access log snippet from nginx.
TEST_LOG_SHORT1 = <<eos
127.0.0.1 - - [12/May/2012:22:53:09 -0700] "GET / HTTP/1.1" 200 1168 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
127.0.0.1 - - [12/May/2012:22:53:09 -0700] "GET /static/css/thirdparty/reset.css HTTP/1.1" 200 639 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
1.3.5.7 - - [12/May/2012:22:53:09 -0700] "GET /static/css/base.css HTTP/1.1" 200 501 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
11.10.9.8 - - [13/May/2012:22:53:09 -0700] "GET /static/css/footer.css HTTP/1.1" 200 536 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
127.127.127.127 - - [14/May/2012:22:53:09 -0700] "GET /static/css/splash.css HTTP/1.1" 200 756 "http://localhost:11080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
eos

EXPECTED_SHORT1 = {
    TEST_DATE_MAY12 => Set.new(%w(127.0.0.1  1.3.5.7)),
    Date.new(2012, 5, 13) => Set.new(%w(11.10.9.8)),
    Date.new(2012, 5, 14) => Set.new(%w(127.127.127.127)),
}

TEST_LOG_REPEATED_ADDR = <<eos
Hidden a bit 38.32.1.99 - - [12/May/2012:22:53:09 -0700] "GET / HTTP/1.1" 200 1168 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
33.32.31.1 - - [12/May/2012:22:53:09 -0700] "GET /127.0.0.1 HTTP/1.1" 200 1168 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19"
eos
EXPECTED_REPEATED_ADDR = {
    TEST_DATE_MAY12 => Set.new(%w(38.32.1.99  33.32.31.1))
}

class AuxiliaryParsersTest < Test::Unit::TestCase
  def setup
    @parser = LogParser.new
  end

  def test_extract_date
    actual = @parser.send(:extract_match, TIMESTAMP_RE, '127.0.0.1 - - [12/May/2012:22:53:09 -0700] "GET / HTTP/1.1"')
    assert_equal(TEST_DATE_MAY12.strftime(DATE_FORMAT), actual)
  end

  def test_parse_short1
    actual = @parser.parse_log(TEST_LOG_SHORT1)
    assert_equal(EXPECTED_SHORT1, actual)
  end

  def test_parse_repeated_address
    actual = @parser.parse_log(TEST_LOG_REPEATED_ADDR)
    assert_equal(EXPECTED_REPEATED_ADDR, actual)
  end
end
