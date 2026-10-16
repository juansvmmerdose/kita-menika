import urllib.request

redirects = {
    "jawara_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5eGzg_pWr665cOyeZz2CR4OJWTsPHdr7XLc6rIa3KKGBdHTAf63XUKzqHSrI8QR8uzSYs7VXv6bGed3CeRQiCjbilo5C5dPcvocSZKWwYLxUNIO49JFXdTBgkkeKWW4o=",
    "jawara_2": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETWmyANIVatvJ_oYIJqTdhNrv80qKSDJm2kbNoC04e8DrN4VGSPjaiYhMwF-K_oPq1vsqKVh-HKKSyDPoqeWszd9eciKJe0drxemhzs6pF20feUxKDXabt_AeXwrE=",
    "sandi_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyP3yZyV6mR4GnKt6shvShyLecpvARmZtMic4tGISuy1TAADafKlN3ZMzGDDi7Io0MGqOr6050Xqu9mRPTY-Di0OulAuh0ubR-SZvMF8tcuQLSWzVCeIr3JoE=",
    "sandi_2": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH33IPUHg_151UqKEb6mkS-9kIV8CCHD3qUqk7WnPo9nvfJwr4kEU3uZUgs6Day-TXt4QGkCJXKA0NvW6GCnyWrop2tADYicrirdVUs76-R5rr9BtGiGPVJZHMzZQuKsbdN11g=",
    "kitakancerita_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtGgyG7P9d9iNr814gqxURKnWAOTIlo9BHSEcqrXNz89LMYlkDzjkfFlNDJu_lodFlgFH_VozptypNlvWt8cQ62X9KhQQuNUVDYvNSZ2OrelLuukHy3_GlEeightc=",
    "kitakancerita_2": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBpCFkehv3TvlLi99smqKKYfzjw-vHqiu6Csz2YQmTGqPtME5nuG36Jbdc5mEPw7zvv7G0ocCV93jvMLLBneFjWvKvP2d5y5RHgBrKPzNVh5y2sMz1YvDCiI2bTlM=",
    "kitakancerita_3": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQtuvCena9ywF8Jbxyv96KPUJNX77gR9JeDTVoZ26rE1idY55SjLRpSm87D2OfvmF-hXIvbu0BUvuC7LOWPmbANbBFjEedhqx5zPzgTaf5WwpAPOnJBNDUXIZPm-k=",
    "thenijo_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKdMLAj3osACLpZnFG2lOTzAYmcFgsxtigG_Bqu1mz0m5WjwdmARtJQawwXXW6njrGMztHCx_ACfHOMXS4tKc8ZqMwdaa_F7Cyawhue5ZEQIlW-bKQOWwAxuDjPXv3",
    "neiscala_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFu_he3usaCxv4psRagTAnMBGU-F8eCEm8IId-6edfe6Vf8YaBj7vlA8iM3V-t6FGtsYYY8Rv4VNDTCrTqb0B4rVDkPCL1ltEczP1S5VSf0sXU2vVmUGEebA_7HS__xj8p",
    "neiscala_2": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-1eu5QQNhu0hBmo8vK2_ITUgqLiD1KhvMcWkXmfrtyJAnUqYABJrwoOylPJ7ctGvVcr2dJJkFW64d3B_XoffMgA2dSwkD1xuKhb19k6Xe6elgHydOhJbW_niltvoX",
    "neiscala_3": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV3hernwj_rDnHam4ELmpyQHO_bx5dqPXYravttfOqS67lc-XNpJ4Qte4GlW2tA5tVHKwHpi26qQvwR2hHnc0U2qf9sOuh7utFsqY6uD4jrD6M4sVqdgnrKUVxluPKQuJC6E_W-VSvdHIifyw=",
    "lunanouva_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJi3m5pykdOa5n46zgTKa14nSte02GNVEdh3D5kwz1ILLm8oa9nEN0VZ3R9eAbmJLKaXpefflYs_1F8lP37aIJOHGqNsIs9TxGI3snX_rVSBOU0E-27dU_UDCmqBq8a_WndA==",
    "lunanouva_2": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmo3qMklE5x7L_hXt85eY9G8hrdDxMmSYIhGfeGwv-36Hhg2dZfNmXvfNKzRt4EvLllNhN6nDhEroLHsVqKjzQ6riFya7dtpkOoomFOkpLs8OBByl-oNvgyUMW4RdhQ7GdwA==",
    "lunanouva_3": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmRK48OtfCdOjLCl7HB6zkuNibzXROTj-M0AnRQdIZmQki0RZUeffddr9SQ-b8Pb3FRbkltkTkzlDpUZESEkDIs0pNu3kWE9U3AAAO5p0J9Yx3_V-Rq1qALxgw6pkKlwMp",
    "luxvisual_1": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLXuhjPI7q8XCZJgN7C8KzmaOQAQyNojGuX9CDCUuiEs3IzIqnyjD0WtPSI62qCqC_l5A9BY5vlsNFxjfZ7YjnL30llJmIoFBDnjjorHTRlae0oA32wkW7JyWdgetWbuuwWumiuMJofSyeng=="
}

for name, u in redirects.items():
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"{name}: {resp.geturl()}")
    except Exception as e:
        print(f"{name} err: {e}")
