#include "lists.h"

/**
 * find_in_list - searches for an item in the list
 * @list - the list
 * @n: the search item
 * Return: 1 if search item found and 0 otherwise
 */
int find_in_list(listint_t *list, int n)
{
	listint_t *curr = list;

	while (curr != NULL)
	{
		if (curr->n == n)
			return (1);
		curr = curr->next;
	}
	return (0);	
}

/**
 * check_cycle - checks if a list has a cycle in it
 * @list: the list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *visited = NULL;
	
	while (curr != NULL)
	{
		if (find_in_list(visited, (unsigned long)curr) == 1)
			return (1);
		add_nodeint(&visited, (unsigned long)curr);
		curr = curr->next;
	}
	return (0);
}
