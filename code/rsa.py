from os.path import join

from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


def generate_key(dir_path: str = ""):
    filepath_private = join(dir_path, "private.pem")
    filepath_receiver = join(dir_path, "receiver.pem")

    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open(filepath_private, "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open(filepath_receiver, "wb")
    file_out.write(public_key)
    file_out.close()


def encrypt_data():
    data = "I met aliens in UFO. Here is the map.".encode("utf-8")
    file_out = open("encrypted_data.bin", "wb")

    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    file_out.close()


class CryptoTest(object):
    pass


if __name__ == '__main__':
    ...
