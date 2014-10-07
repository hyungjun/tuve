if __name__ == "__main__":
    import sys
    from util.path import app_path
    sys.path.append(app_path.as_posix())

    from tuve import command
    command.autorun()
