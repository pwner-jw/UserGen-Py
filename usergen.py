import sys
import os

def generate_names(full_name, selected_format=None):
    nlist = full_name.lower().strip().split(" ")
    if len(nlist) < 2:
        return []

    first, last = nlist[0], nlist[1]
    formats = {
        "first": first,
        "last": last,
        "firstlast": first + last,
        "lastfirst": last + first,
        "first.last": f"{first}.{last}",
        "firstlast1": first + last[0],
        "first1last": first[0] + last,
        "last1first": last[0] + first,
        "last1.first": f"{last[0]}.{first}",
        "lastfirst1": last + first[0],
        "last.first1": f"{last}.{first[0]}",
        "last.first": f"{last}.{first}",
        "first1last1": first[0] + last[0],
        "first4last4": first[:4] + last[:4],
        "first1last7": first[:1] + last[:7],
        "firstlast8": (first + last)[:8]
    }

    if selected_format:
        return [formats.get(selected_format)] if formats.get(selected_format) else []
    return sorted(set(formats.values()))

def show_help():
    print("""
Usage:
  python3 script.py <firstname> <lastname>
  python3 script.py --input-file names.txt
  python3 script.py --input-file names.txt --select-format first.last
  python3 script.py --recognise j.smith "john smith"

Options:
  --input-file <file>      Read names from a file
  --select-format <fmt>    Only output a specific format
  --recognise <user> <name> Identify which format matches a known username
  --help                   Show this menu
    """)

if __name__ == "__main__":
    args = sys.argv

    if "--help" in args or len(args) == 1:
        show_help()
        sys.exit(0)

    if "--recognise" in args:
        idx = args.index("--recognise")
        target = args[idx + 1].lower()
        name = args[idx + 2] if len(args) > idx + 2 else "john smith"
        nlist = name.lower().split(" ")
        if len(nlist) >= 2:
            f, l = nlist[0], nlist[1]
            test_fmts = {
                "first": f, "last": l, "firstlast": f+l, "lastfirst": l+f,
                "first.last": f"{f}.{l}", "firstlast1": f+l[0], "first1last": f[0]+l,
                "last1first": l[0]+f, "last1.first": f"{l[0]}.{f}", "lastfirst1": l+f[0],
                "last.first1": f"{l}.{f[0]}", "last.first": f"{l}.{f}",
                "first1last1": f[0]+l[0], "first4last4": f[:4]+l[:4],
                "first1last7": f[:1]+l[:7], "firstlast8": (f+l)[:8]
            }
            for fmt, val in test_fmts.items():
                if val == target:
                    print(f"Format found: {fmt}")
                    sys.exit(0)
        print("Format not recognized.")
        sys.exit(0)

    fmt = args[args.index("--select-format") + 1] if "--select-format" in args else None

    if "--input-file" in args:
        fname = args[args.index("--input-file") + 1]
        if os.path.exists(fname):
            with open(fname, "r") as f:
                for line in f:
                    for u in generate_names(line, fmt):
                        if u: print(u)
    else:
        name_args = [a for a in args[1:] if not a.startswith("-") and a != fmt]
        if len(name_args) >= 2:
            for u in generate_names(" ".join(name_args), fmt):
                if u: print(u)
