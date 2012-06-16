require 'test/unit'

class Quicksort
  def sort(values)
    results = Array.new(values)
    sort!(results)
    results
  end

  def sort!(values)
    sort_impl(0, values.length-1, values)
    values
  end

  private

  def partition(start_index, end_index, values)
    pivot = values[end_index]
    i = start_index - 1
    (start_index..end_index-1).each do |j|
      if values[j] <= pivot
        i += 1
        values[i], values[j] = values[j], values[i]
      end
    end

    i += 1
    values[i], values[end_index] = values[end_index], values[i]
    i
  end

  def sort_impl(start_index, end_index, values)
    if start_index >= end_index
      return
    end
    pivot_index = partition(start_index, end_index, values)
    sort_impl(start_index, pivot_index-1, values)
    sort_impl(pivot_index+1, end_index, values)
  end
end

class QuicksortTest < Test::Unit::TestCase
  def setup
    @qs = Quicksort.new
  end

  def call_sort(values)
    expected = values.sort
    actual = @qs.sort(values)
    assert_equal(expected, actual, "Failed to sort values: #{values}")
  end

  def test_sort_multi_ints
    call_sort((0..31).to_a.shuffle!)
  end

  def test_sort_three_ints
    call_sort([0,1,2].shuffle!)
  end

  def test_sort_two_ints
    call_sort([1,0])
  end

  def test_sort_single_int
    call_sort([0])
  end

  def test_sort_in_place
    values = (0..31).to_a.shuffle!
    previous = Array.new(values)
    expected = values.sort
    @qs.sort!(values)
    assert_equal(expected, values, "Failed to sort values: #{previous}")
    assert_not_equal(previous, values)
  end
end

