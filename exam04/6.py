def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []
    names = list(packages)
    names.sort()

    while len(result) < len(packages):
        found = False

        for package in names:
            if package in result:
                continue

            ready = True

            for dependency in packages[package]:
                if dependency in packages and dependency not in result:
                    ready = False
                    break

            if ready:
                result.append(package)
                found = True

        if not found:
            return []

    return result

print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
print(package_dependency_resolver({}))
print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))