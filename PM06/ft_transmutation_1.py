# import 
# # transmutationを直接インポートし、錬金術をなしとげる.transmutationはalchemyを経由しないと見えないので、
# alchemy.をつける必要がある。import alchemy.transmutation は、呼び出すときにalchemy.trasmutation.lead_to_gold()のように長くなってしまう。
from alchemy import transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.lead_to_gold()}")

if __name__ == "__main__":
    main()