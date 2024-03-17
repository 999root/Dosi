
import Spoofer
import Check
import Cache

# Define the textLogo
textLogo = r"""   
                ---.      .---
                    '.  .'
                     '.'
                     /
                    /
                   /
                  /
                 /
                /
               /
              /
            .'.
          .'   \
        .'     |
      .'       \
 ..--/_________|.--.
// '----------'//  \\
||'=:='=:='=:='||()||
\\_'--''--''--'\\__//
 `--' HWIDMower `--`
  """

def main():
    while True:
        print(textLogo)
        print("  ┌ FUNCS ──────────────────────────────────┐")
        print("  │ [!hwid] Spoof HWID                      │")
        print("  │ [!guid] Spoof Guid                      │")
        print("  │ [!pcname] Spoof your Computer Name      │")
        print("  │ [!productid] Spoof ProductId            │")
        print("  │                                         │")
        print("  │ [!check] Check Registry Keys            │")
        print("  │ [!purge] Purge Valorant/Ubisoft Cache   │")
        print("  └─────────────────────────────────────────┘")
        choice = input("  >>> ")
        if choice == "!hwid":
            Spoofer.HWID.Spoof()
        elif choice == "!guid":
            Spoofer.GUID.Spoof()
        elif choice == "!pcname":
            Spoofer.PCNAME.Spoof()
        elif choice == "!productid":
            Spoofer.PRODUCTID.Spoof()
        elif choice == "!check":
            Check.check_registry_keys()
        elif choice == "!purge":
            Cache.clear_ubisoft_cache()
            Cache.clear_valorant_cache()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
