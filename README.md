# python-dijkstra

Dijkstra... en Python!


## Instructions

Copiez votre code dans les différentes fonctions de `dijkstra.py`.

Attention, il ne faut pas changer le nom de la fonction. Vous pouvez changer les arguments,
mais la fonction doit fonctionner avec le nombre initial d'arguments. Par exemple, vous
pouvez changer `def reachables(grap, s)` en `def reachables(graph, s, foo=None, bar=2)`.

Exécutez les tests en local (cf ci-dessous).

Quand le résultat est satisfaisant, git add, git commit, git push:

```shell
$ git add dijkstra.py
$ git commit --message "parse graph, v1"
$ git push
```

## Exécuter les tests localement

```shell
$ python grader.py
```

Il est courant de se tromper et de faire des boucles infinies dans son code. Dans ce cas,
les tests n'arriveront jamais "au bout". Appuyez sur `Ctrl + C` pour interrompre le grader.
