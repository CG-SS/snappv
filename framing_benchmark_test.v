module snappv

import benchmark
import os

fn test_benchmark_framing_alice() {
	alice := os.read_bytes('alice29.txt')!

	mut b := benchmark.start()

	encode_stream(alice)

	b.measure('framing_alice')
}
