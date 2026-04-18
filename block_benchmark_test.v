module snappv

import benchmark
import os

fn test_benchmark_block_alice() {
	alice := os.read_bytes('alice29.txt')!

	mut b := benchmark.start()

	compress(alice)

	b.measure('block_alice')
}
