from bert_test.src import extract_features

if __name__ == "__main__":
    print('prog began')
    brt = extract_features.BERT(
        '/home/paya/Desktop/Link-to-Research/Shared/bert/uncased_L-24_H-1024_A-16/vocab.txt',
        '/home/paya/Desktop/Link-to-Research/Shared/bert/uncased_L-24_H-1024_A-16/bert_config.json',
        '/home/paya/Desktop/Link-to-Research/Shared/bert/uncased_L-24_H-1024_A-16/bert_model.ckpt'
    )
    temp = brt.get_vectors(["i see you", "you saw him"], True)

    print('prog ended')




