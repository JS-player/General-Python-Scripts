import math

def average_code_length(codewords, probabilities):
    acc = 0
    for codeword, probability in zip(codewords, probabilities):
        acc += len(codeword) * probability
    return acc

def entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities)

def code_efficiency(entropy, avg_code_length):
    return entropy / avg_code_length

def compression_ratio(original_size, compressed_size):
    return original_size / compressed_size

if __name__ == "__main__":
    example_codewords = ["0", "10", "110", "111"]
    example_probabilities = [0.5, 0.25, 0.125, 0.125]

    avg_code_length = average_code_length(example_codewords, example_probabilities)
    ent = entropy(example_probabilities)
    efficiency = code_efficiency(ent, avg_code_length)

    original_size = 8 # Example: original size in bits
    compressed_size = len("".join(example_codewords)) # Example: compressed size in bits
    compression = compression_ratio(original_size, compressed_size)

    print("Average code length:", avg_code_length)
    print("Entropy:", ent)
    print("Code efficiency:", efficiency)
    print("Compression ratio:", compression)
