# 魔法のアーティファクトを「power」で降順ソートする
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


# パワーが min_power 以上のメイジだけを抽出する
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


# 呪文名に "* " を前後につける
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


# max/min/average を計算しpowerの値だけ返す
# max(mages, key=lambda m: m['power'])だけだと辞書そのものキー込みで返ってしまう。
def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(mages, key=lambda m: m['power'])['power']
    min_power: int = min(mages, key=lambda m: m['power'])['power']
    avg_power: float = round(sum(m['power'] for m in mages) / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }

def main() -> None:
    artifacts = [
        {'name': 'Water Chalice', 'power': 104, 'type': 'armor'},
        {'name': 'Storm Crown', 'power': 113, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 102, 'type': 'accessory'},
        {'name': 'Wind Cloak', 'power': 95, 'type': 'armor'}
    ]
    mages = [
        {'name': 'Sage', 'power': 86, 'element': 'water'},
        {'name': 'Ember', 'power': 81, 'element': 'light'},
        {'name': 'Alex', 'power': 70, 'element': 'wind'},
        {'name': 'Sage', 'power': 51, 'element': 'fire'},
        {'name': 'Casey', 'power': 99, 'element': 'wind'}
    ]
    spells = ['freeze', 'earthquake', 'fireball', 'tsunami']

    print("Testing artifact sorter...")
    a_s: list[dict] = artifact_sorter(artifacts)
    print(
        f" {a_s[0]['name']} ({a_s[0]['power']} power) comes before "
        f"{a_s[1]['name']} ({a_s[1]['power']} power)"
    )

    print("Testing spell transformer...")
    s_t: list[str] = spell_transformer(spells)
    for spell in s_t:
        print(" ", spell)

    print("Testing power filter...")
    p_f: list[dict] = power_filter(mages, 80)
    for mage in p_f:
        print(
            f" Name: {mage['name']}, "
            f" Power: {mage['power']}, "
            f" Element: {mage['element']}"
        )

    print("\nTesting mage stats...")
    m_s: dict = mage_stats(mages)
    print(f" Max Power: {m_s['max_power']}")
    print(f" Min Power: {m_s['min_power']}")
    print(f" Avg Power: {m_s['avg_power']}")


if __name__== "__main__":
    main()