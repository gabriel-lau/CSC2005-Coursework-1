# INTERFACE BETWEEN GUI AND THE STEGANOGRAPHY MODULES
import imgSteganography as img
import docSteganography as doc
import avSteganography as av

def encode(text, bits, fileName): # encode(text, bit, fileName) -> fileName
    if fileName.endswith(('.mp3', '.mp4', '.wav')):
        return av.encode_av(fileName, text, bits)
    if fileName.endswith(('.png')):
        return img.encode_image(fileName, text, bits)
    if fileName.endswith(('.txt','.docx','.xlsx')):
        return doc.encode_doc(fileName, text, bits)
    return fileName

def decode(bits, fileName): # decode(bit, fileName) -> text
    if fileName.endswith(('.mp3', '.mp4', '.wav')):
        return av.decode_av(fileName, bits)
    if fileName.endswith(('.png')):
        return img.decode_image(fileName, bits)
    if fileName.endswith(('.txt','.docx','.xlsx')):
        return doc.decode_doc(fileName, bits)
    return fileName