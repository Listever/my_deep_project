import tensorflow as tf


def create_hparams():
    params = tf.contrib.training.HParams(
        num_units = 256, # Network size
        num_layers = 2, # Network depth
        attention_type = 'luong', #  luong | bahdanau | None
        attention_architecture = 'standard', # standard | gnmt
        optimizer = 'sgd', # sgd , adam
        learning_rate = 1., # sgd:1, Adam:0.0001
        decay_steps = 100,
        decay_rate = 0.99,
        epochs = 50,
        out_dir = 'logs/model',
        # vocab
        encoder_vocab_size = 50,
        decoder_vocab_size = 50,
        share_vocab = False,
        # Sequence lengths
        src_max_len = 50,
        tgt_max_len = 50,
        # Default settings works well (rarely need to change)
        unit_type = 'lstm', # lstm | gru | rnn
        keep_prob = 0.8,
        max_gradient_norm = 1,
        batch_size = 8,
        num_gpus = 1,
        metrics = None,
        time_major = True,
        # inference
        infer_mode = 'greedy', # greedy | beam_search
        beam_width = 0,
        num_translations_per_input = 10)
    return params
