class DirectDownloadLinkException(Exception):
    """Tidak ditemukan metode yang mendukung pengekstrakan"""
    pass


class NotSupportedExtractionArchive(Exception):
    """Tipe arsip tidak mendukung pengekstrakan"""
    pass
