# -*- coding: utf-8 -*-
"""
pytube.itags
~~~~~~~~~~~~

This module contains a lookup table of YouTube's format identifier codes
(itags) to some additional meta data not specified in the media manifest.
"""

ITAGS = {
    5: ('240p', '64kbps', 'H.263', None, 30),
    6: ('270p', '64kbps', 'H.263', None, 30),
    13: ('144p', None, 'mp4v', None, 30),
    17: ('144p', '24kbps', 'mp4v', None, 30),
    18: ('360p', '96kbps', 'H.264', None, 30),
    22: ('720p', '192kbps', 'H.264', None, 30),
    34: ('360p', '128kbps', 'H.264', None, 30),
    35: ('480p', '128kbps', 'H.264', None, 30),
    36: ('240p', None, 'mp4v', None, 30),
    37: ('1080p', '192kbps', 'H.264', None, 30),
    38: ('3072p', '192kbps', 'H.264', None, 30),
    43: ('360p', '128kbps', 'VP8', None, 30),
    44: ('480p', '128kbps', 'VP8', None, 30),
    45: ('720p', '192kbps', 'VP8', None, 30),
    46: ('1080p', '192kbps', 'VP8', None, 30),
    59: ('480p', '128kbps', 'H.264', None, 30),
    78: ('480p', '128kbps', 'H.264', None, 30),
    82: ('360p', '128kbps', 'H.264', '3D', 30),
    83: ('480p', '128kbps', 'H.264', '3D', 30),
    84: ('720p', '192kbps', 'H.264', '3D', 30),
    85: ('1080p', '192kbps', 'H.264', '3D', 30),
    91: ('144p', '48kbps', 'H.264', 'HLS', 30),
    92: ('240p', '48kbps', 'H.264', 'HLS', 30),
    93: ('360p', '128kbps', 'H.264', 'HLS', 30),
    94: ('480p', '128kbps', 'H.264', 'HLS', 30),
    95: ('720p', '256kbps', 'H.264', 'HLS', 30),
    96: ('1080p', '256kbps', 'H.264', 'HLS', 30),
    100: ('360p', '128kbps', 'VP8', '3D', 30),
    101: ('480p', '192kbps', 'VP8', '3D', 30),
    102: ('720p', '192kbps', 'VP8', '3D', 30),
    132: ('240p', '48kbps', 'H.264', 'HLS', 30),
    151: ('720p', '24kbps', 'H.264', 'HLS', 30),

    # DASH Video
    133: ('240p', None, 'H.264', 'video', 30),
    134: ('360p', None, 'H.264', 'video', 30),
    135: ('480p', None, 'H.264', 'video', 30),
    136: ('720p', None, 'H.264', 'video', 30),
    137: ('1080p', None, 'H.264', 'video', 30),
    138: ('2160p', None, 'H.264', 'video', 30),
    160: ('144p', None, 'H.264', 'video', 30),
    167: ('360p', None, 'VP8', 'video', 30),
    168: ('480p', None, 'VP8', 'video', 30),
    169: ('720p', None, 'VP8', 'video', 30),
    170: ('1080p', None, 'VP8', 'video', 30),
    212: ('480p', None, 'H.264', 'video', 30),
    218: ('480p', None, 'VP8', 'video', 30),
    219: ('480p', None, 'VP8', 'video', 30),
    242: ('240p', None, 'VP9', 'video', 30),
    243: ('360p', None, 'VP9', 'video', 30),
    244: ('480p', None, 'VP9', 'video', 30),
    245: ('480p', None, 'VP9', 'video', 30),
    246: ('480p', None, 'VP9', 'video', 30),
    247: ('720p', None, 'VP9', 'video', 30),
    248: ('1080p', None, 'VP9', 'video', 30),
    264: ('144p', None, 'H.264', 'video', 30),
    266: ('2160p', None, 'H.264', 'video', 30),
    271: ('144p',  None, 'VP9', 'video', 30),
    272: ('2160p', None, 'VP9', 'video', 30),
    278: ('144p', None, 'VP9', 'video', 30),
    298: ('720p', None, 'H.264', 'video', 60),
    299: ('1080p', None, 'H.264', 'video', 60),
    302: ('720p', None, 'VP9', 'video', 60),
    303: ('1080p', None, 'VP9', 'video', 60),
    308: ('1440p', None, 'VP9', 'video', 60),
    313: ('2160p', None, 'VP9', 'video', 30),
    315: ('2160p', None, 'VP9', 'video', 60),

    # DASH Audio
    139: (None, '48kbps', None, 'audio', None),
    140: (None, '128kbps', None, 'audio', None),
    141: (None, '256kbps', None, 'audio', None),
    171: (None, '128kbps', None, 'audio', None),
    172: (None, '256kbps', None, 'audio', None),
    249: (None, '50kbps', None, 'audio', None),
    250: (None, '70kbps', None, 'audio', None),
    251: (None, '160kbps', None, 'audio', None),
    256: (None, None, None, 'audio', None),
    258: (None, None, None, 'audio', None),
    325: (None, None, None, 'audio', None),
    328: (None, None, None, 'audio', None),
}


def get_format_profile(itag):
    """Returns additional format information for a given itag.

    :param str itag:
        YouTube format identifier code.
    """
    res, bitrate, vcodec, note, fps = ITAGS[int(itag)]
    return {
        'resolution': res,
        'abr': bitrate,
        'fmt_note': note,
        'fps': fps,
    }
