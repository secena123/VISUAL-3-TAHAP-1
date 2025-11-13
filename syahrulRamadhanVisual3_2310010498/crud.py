# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
        self.koneksiDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_perkantoran'
        )

    def simpanSatuan(self, id_satuan, kode, nama):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO satuan (id, kode, nama) VALUES (%s, %s, %s)"
        val = (id_satuan, kode, nama)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahSatuan(self, id_satuan, kode, nama):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE satuan SET kode=%s, nama=%s WHERE id=%s"
        val = (kode, nama, id_satuan)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusSatuan(self, id_satuan):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM satuan WHERE id=%s", (id_satuan,))
        self.koneksiDB.commit()
        kursor.close()

    def dataSatuan(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM satuan ORDER BY id ASC")
        return kursor.fetchall()

    def simpanBarang(self, id_brg, kode, nama, ket, stok_awal, stok, id_satuan, rek, status, adm, staf, tgl):
        kursor = self.koneksiDB.cursor()
        sql = """INSERT INTO barang (id, kode, nama, keterangan, stok_awal, stok, satuan_id, rekomendasi, status, admin_view, staf_view, tanggal_update)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        val = (id_brg, kode, nama, ket, stok_awal, stok, id_satuan, rek, status, adm, staf, tgl)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahBarang(self, id_brg, kode, nama, ket, stok_awal, stok, id_satuan, rek, status, adm, staf, tgl):
        kursor = self.koneksiDB.cursor()
        sql = """UPDATE barang SET kode=%s, nama=%s, keterangan=%s, stok_awal=%s, stok=%s, satuan_id=%s,
                 rekomendasi=%s, status=%s, admin_view=%s, staf_view=%s, tanggal_update=%s WHERE id=%s"""
        val = (kode, nama, ket, stok_awal, stok, id_satuan, rek, status, adm, staf, tgl, id_brg)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusBarang(self, id_brg):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM barang WHERE id=%s", (id_brg,))
        self.koneksiDB.commit()
        kursor.close()

    def dataBarang(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM barang ORDER BY id ASC")
        return kursor.fetchall()

    def simpanPesanan(self, id_pesan, id_mkt, id_staf, id_brg, minta, kirim, tgl_minta, tgl_kirim, status, rek, stat_rek):
        kursor = self.koneksiDB.cursor()
        sql = """INSERT INTO pesanan (id, marketing_id, staf_id, barang_id, permintaan, pengiriman,
                 tanggal_minta, tanggal_kirim, status, rekomendasi, status_rekomendasi)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        val = (id_pesan, id_mkt, id_staf, id_brg, minta, kirim, tgl_minta, tgl_kirim, status, rek, stat_rek)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahPesanan(self, id_pesan, id_mkt, id_staf, id_brg, minta, kirim, tgl_minta, tgl_kirim, status, rek, stat_rek):
        kursor = self.koneksiDB.cursor()
        sql = """UPDATE pesanan SET marketing_id=%s, staf_id=%s, barang_id=%s, permintaan=%s, pengiriman=%s,
                 tanggal_minta=%s, tanggal_kirim=%s, status=%s, rekomendasi=%s, status_rekomendasi=%s WHERE id=%s"""
        val = (id_mkt, id_staf, id_brg, minta, kirim, tgl_minta, tgl_kirim, status, rek, stat_rek, id_pesan)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusPesanan(self, id_pesan):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM pesanan WHERE id=%s", (id_pesan,))
        self.koneksiDB.commit()
        kursor.close()

    def dataPesanan(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM pesanan ORDER BY id ASC")
        return kursor.fetchall()

    def simpanRiwayat(self, id_rw, id_user, id_brg, jenis, qty, ket, tgl):
        kursor = self.koneksiDB.cursor()
        sql = """INSERT INTO riwayat (id, user_id, barang_id, jenis, qty, keterangan, tanggal)
                 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        val = (id_rw, id_user, id_brg, jenis, qty, ket, tgl)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahRiwayat(self, id_rw, id_user, id_brg, jenis, qty, ket, tgl):
        kursor = self.koneksiDB.cursor()
        sql = """UPDATE riwayat SET user_id=%s, barang_id=%s, jenis=%s, qty=%s, keterangan=%s, tanggal=%s
                 WHERE id=%s"""
        val = (id_user, id_brg, jenis, qty, ket, tgl, id_rw)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusRiwayat(self, id_rw):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM riwayat WHERE id=%s", (id_rw,))
        self.koneksiDB.commit()
        kursor.close()

    def dataRiwayat(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM riwayat ORDER BY id ASC")
        return kursor.fetchall()
